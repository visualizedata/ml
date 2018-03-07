import os
import pandas as pd
import json
import zipfile
import sys

def submission_checker(fp):
    global final_script
    final_script = ''
    fpt = fp + '/tests' # path for extracted files
    try:
        os.mkdir( fpt, 0o777 ) # create subdirectory for extracted files
    except FileExistsError:
        print('test subdirectory already exists') # unless it already exists
        
    def get_zip_name():
        '''Get the name of the zip file in the specified directory. Make sure only one zip file in the specified directory.'''
        zf = '' # name of zip file
        files = files = [f for f in os.listdir(fp) if os.path.isfile(os.path.join(fp, f))]
        n_zips = 0
        for f in files:
            if (f.split('.')[1] == 'zip'):
                zf = f
                n_zips += 1
            if n_zips > 1:
                raise ValueError('There is more than one zip file in this directory. It should only include a single zip file.')
        return(zf)
    
    def un_zip_file():
        '''Unzip the submission file'''
        zip_file = get_zip_name()
        if zip_file == '':
            raise ValueError('There is no zip file in the specified directory.')
        zffp = fp + '/' + zip_file
        zip_ref = zipfile.ZipFile(zffp, 'r')
        zip_ref.extractall(fpt)
        zip_ref.close()
        print(zip_file + ' unzipped')
        
    un_zip_file()
    
    def get_ipynb_name():
        '''Get the name of the ipynb file in the specified directory. Make sure only one ipynb file in the specified directory.'''
        zf = '' # name of file
        files = files = [f for f in os.listdir(fpt) if os.path.isfile(os.path.join(fpt, f))]
        n_zips = 0
        for f in files:
            if (f.split('.')[1] == 'ipynb'):
                zf = f
                n_zips += 1
            if n_zips > 1:
                raise ValueError('There is more than one ipynb file in this directory. It should only include a single ipynb file.')
        return(zf)

    ipynb_file = get_ipynb_name()
    print('Submission notebook: ' + ipynb_file)
    
    def read_notebook():
        '''Read the contents of the Jupyter Notebook.'''
        sub_file = fpt + "/" + ipynb_file 
        jnb  = open(sub_file, "r")
        return(jnb.read())
    
    jnb_json = (read_notebook())
    
    def check_files():
        '''Check the contents of the extracted zip file, for correct file types and expected number of files.'''
        files = files = [f for f in os.listdir(fpt) if os.path.isfile(os.path.join(fpt, f))]
        ft_allowed = ['ipynb', 'pkl', 'py']
        for f in files:
            if f.split('.')[1] not in ft_allowed:
                raise ValueError('Invalid file type; only .ipynb, .pkl, and .py file extensions permitted')
            if f.split('.')[1] == 'py':
                if f.split('.')[0] != 'my_measures':
                    print('WARNING: Invalid .py file; `my_measures.py` is the only .py file permitted')

    check_files()
    
    def initial_checks():
        '''Initial checks for fits, CSV reads, and computation of performance measures.'''
        x = json.loads(jnb_json)
        has_cm = False
        has_readcsv = False
        has_fit = False
        probs = ''
        for cell in x['cells']:
            if cell['cell_type'] == "code":
                for l in cell['source']:
                    if l.find('.fit') >= 0:
                        if l.find('#') < 0 or (l.find('#') >= 0 and l.find('.fit') < l.find('#')):
                            if has_fit == False:
                                has_fit = True
                                probs += "You are using a FIT method; this is prohibited; you can only use transform methods in the submission. "
                    if l.find('.compute_measures()') >= 0:
                        if l.find('#') < 0 or (l.find('#') >= 0 and l.find('.compute_measures()') < l.find('#')):
                            if has_cm == True:
                                probs += "You are computing performance measures more than once and I don't know which to use. "
                            if has_cm == False:
                                has_cm = True
                    if l.find('read_csv') >= 0:
                        if l.find('#') < 0 or (l.find('#') >= 0 and l.find('read_csv') < l.find('#')):
                            if has_readcsv == True:
                                probs += "You are reading more than one CSV file, but should only be reading one. "
                            if has_readcsv == False:
                                has_readcsv = True
        if has_cm == False:
            probs += "Performance measures are not being computed. "
        if has_readcsv == False:
            probs += "No CSV file is being read. "
        if len(probs) > 1:
            raise ValueError(probs)

    initial_checks()
   
    # create and execute input code
    final_script = """
class BinaryClassificationPerformance():
    '''Performance measures to evaluate the fit of a binary classification model, v1.01'''

    def __init__(self, predictions, labels, desc, probabilities=None):
        '''Initialize attributes: predictions-vector of predicted values for Y, labels-vector of labels for Y'''
        '''probabilities-optional, probability that Y is equal to True'''
        self.probabilities = probabilities
        self.performance_df = pd.concat([pd.DataFrame(predictions), pd.DataFrame(labels)], axis=1)
        self.performance_df.columns = ['preds', 'labls']
        self.desc = desc
        self.performance_measures = {}
        self.image_indices = {}

    def compute_measures(self):
        '''Compute performance measures defined by Flach p. 57'''
        self.performance_measures['Pos'] = self.performance_df['labls'].sum()
        self.performance_measures['Neg'] = self.performance_df.shape[0] - self.performance_df['labls'].sum()
        self.performance_measures['TP'] = ((self.performance_df['preds'] == True) & (self.performance_df['labls'] == True)).sum()
        self.performance_measures['TN'] = ((self.performance_df['preds'] == False) & (self.performance_df['labls'] == False)).sum()
        self.performance_measures['FP'] = ((self.performance_df['preds'] == True) & (self.performance_df['labls'] == False)).sum()
        self.performance_measures['FN'] = ((self.performance_df['preds'] == False) & (self.performance_df['labls'] == True)).sum()
        self.performance_measures['Accuracy'] = (self.performance_measures['TP'] + self.performance_measures['TN']) / (self.performance_measures['Pos'] + self.performance_measures['Neg'])
        self.performance_measures['Precision'] = self.performance_measures['TP'] / (self.performance_measures['TP'] + self.performance_measures['FP'])
        self.performance_measures['Recall'] = self.performance_measures['TP'] / self.performance_measures['Pos']
        self.performance_measures['desc'] = self.desc
    """

    final_script += "os.chdir('" + fpt + "')\n"

    pycode = json.loads(jnb_json)

    def handle_code(c):
        '''Handler for modifications to input code.'''
        global final_script
        if c.find('my_measures.BinaryClassificationPerformance') >= 0:
            c.replace("my_measures.", "")
        if c.find('my_measures') >= 0:
            print('*** skipping read of my_measures module ***')
        elif c.find('read_csv') >= 0:
            final_script += "amazon = pd.read_csv('https://raw.githubusercontent.com/visualizedata/ml/master/resources/test.csv')" + '\n'
            if c.split('=')[0].strip() != 'amazon':
                final_script += x.split('=')[0].strip() + ' = amazon \n'
        elif c.find('import matplotlib.pyplot as plt') >= 0:
            final_script += 'import matplotlib.pyplot as plt \n'
            final_script += "plt.ioff() \n"
        elif c.find('.compute_measures()') >= 0:
            compute_measures_object = c.split('.')[0]
            final_script += c + '\n'
            final_script += 'pm = ' + str(compute_measures_object) +".performance_measures \n"
            # final_script += "print(" + str(compute_measures_object) +".performance_measures) \n"
        elif c.find('plt.show()') >= 0:
            print('*** suppressing plots ***')
        else:
            final_script += c + '\n'

    # iterate through each line of input code to construct new executable code
    for cell in pycode['cells']:
        if cell['cell_type'] == "code":
            for l in cell['source']:
                if len(l) > 1: # ignore blank lines
                    if l[0] != '%' and l[0] != '#': # ignore magic functions and comments
                        if l.find('print') < 0: # ignore prints
                            handle_code(l)

    # final_script += 'print(pm)'
    
    print("------------------------------------------")
    # print(final_script)
    exec(final_script)
    print("------------------------------------------")
    print("SUCCESS!")

submission_checker(sys.argv[1])