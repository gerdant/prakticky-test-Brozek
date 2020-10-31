# script analysing file from CFTR

library(plyr)

cftr <- read.table("Data/cftr.csv", header=TRUE,sep=",")

mut <- cftr[cftr$CFTR_mutace != "c.[=];[=]",]
mut5T12TG = mut[FALSE,]
mut5Tany = mut[FALSE,]
othermut = mut[FALSE,]

# devide into smaller dataframes based on mutations

for(i in 1:nrow(mut)){
  if(grepl("5T,",mut[i,"Poly.T"])){
    if(grepl("5T,12TG",mut[i,"Poly.T"])){
      mut5T12TG <- rbind(mut5T12TG,mut[i,])
    }else{
      mut5Tany <- rbind(mut5Tany,mut[i,])
    }
  }else{
    othermut <- rbind(othermut,mut[i,])
  }
}

# 1) prints number of patients

print("Number of pacients with mutations:")
print(paste("5T(>=12TG) : ", nrow(mut5T12TG)))
print(paste("MUT        : ", nrow(othermut)))
print(paste("MUT + 5T   : ", nrow(mut5Tany)))

# 2) plot pie chart of homozygot and heterozygt number

homozygot = mut[FALSE,]
for(i in 1:nrow(mut)){
  if(grepl("; - ",mut[i,"Poly.T"])){
    homozygot <- rbind(homozygot,mut[i,])
  }
}

slices <- c(nrow(homozygot), nrow(mut))
pct <- round(slices/sum(slices)*100)
lbls <- c("homozygot", "heterozygot")
lbls <- paste(lbls," ", pct,"%")
pie(slices, labels = lbls, main="Poly-T varianta")

# 3) prints number of CFTR variants in file

print(paste("Number of CTFR variants: ",nlevels(cftr$CFTR_mutace)))

# 4) counts how many entries are in each CFTR variant

print(count(cftr$CFTR_mutace))
