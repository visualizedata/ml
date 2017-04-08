#Read in data
hun <- read.csv("/Users/alexpavlakis/Desktop/Data/texting.csv",
                stringsAsFactors = FALSE,
                header = TRUE)

#Pull out all the words
words <- list()
for(i in 1:length(hun$text)){
  words[[i]] <- strsplit(hun$text[i], split = " ")
}

unique.words <- unique(unlist(words))
