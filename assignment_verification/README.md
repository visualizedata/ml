
# Verification of ML Assigment 1 submission file (.zip)

The `ver.py` script in this repository runs tests on your [ML Assignment 1](https://docs.google.com/document/d/1WGYw99e5q6j5V0Zrf2HveagU6URt_kVvdR8B9HYQ99E/edit?usp=sharing) submission file (.zip) to verify it meets the [submission requirements](https://github.com/visualizedata/ml/blob/master/week06/README.md). 

## Instructions for using this script to test your submission .zip file:

1. Save `ver.py` on your local drive, preferably in the directory containing your assignment files.  
2. In the terminal, navigate to the directory where you have saved `ver.py`.  
3. In the terminal, run the `python` command with two arguments: 1) the name of the verification script (`ver.py`) and 2) the full file path of the location of your submission (.zip) file.  

**For example:**  
`python ver.py '/Users/aaronhill/Dropbox/data/ml_new/ML_1_sub_test/hal'`  

*Where `ver.py` is in the present working directory and `/Users/aaronhill/Dropbox/data/ml_new/ML_1_sub_test/hal` contains the contents of my .zip submission.*

**If a .zip file meets the submission requirements, the output to the console will always end with:**  
`SUCCESS!`

**Otherwise, the output will end with errors that describe the problem(s) with the submission file.**

## Example of a successful submission file

```
$ ls
README.md		hal			test_files_for.ipynb
Untitled.ipynb		oops			tests.ipynb
another			test.csv		ver.py
$ python ver.py '/Users/aaronhill/Dropbox/data/ml_new/ML_1_sub_test/hal'
test subdirectory already exists
submission_01.zip unzipped
Submission notebook: _03_submission.ipynb
*** skipping read of my_measures module ***
*** suppressing plots ***
------------------------------------------
/Users/aaronhill/anaconda3/lib/python3.6/site-packages/sklearn/feature_extraction/hashing.py:94: DeprecationWarning: the option non_negative=True has been deprecated in 0.19 and will be removed in version 0.21.
  " in version 0.21.", DeprecationWarning)
------------------------------------------
SUCCESS!
$ 
```

## Example of a submission file that does not meet the requirements:

```
$ python ver.py '/Users/aaronhill/Dropbox/data/ml_new/ML_1_sub_test/oops'
test subdirectory already exists
Archive.zip unzipped
Submission notebook: _01_train.ipynb
Traceback (most recent call last):
  File "ver.py", line 187, in <module>
    submission_checker(sys.argv[1])
  File "ver.py", line 111, in submission_checker
    initial_checks()
  File "ver.py", line 109, in initial_checks
    raise ValueError(probs)
ValueError: You are using a FIT method; this is prohibited; you can only use transform methods in the submission. You are computing performance measures more than once and I don't know which to use. You are computing performance measures more than once and I don't know which to use. You are computing performance measures more than once and I don't know which to use. You are computing performance measures more than once and I don't know which to use. 
$ 
```