# script for GJB2 analysis

path = "Data"

file.names <- dir(path, pattern =".out.csv", full.names = TRUE)
for(file in file.names){
  results <- read.table(file,header=TRUE, sep=",")
  if ("GJB2" %in% results$Gene_refGene){
    
    # to see in which file was variant detected
    #print(file)
    row_i <- which(results$Gene_refGene == "GJB2")
    ref <- strsplit(paste(results$AAChange_refGene[row_i[1]]),"[:]")
    variant <-as.vector(unlist(ref))
    results$variant_frequency[row_i[1]]
    
    # prints if the variant was detected
    
    if (results$variant_frequency[row_i[1]] > 0.2) {
      type <- cut(results$variant_frequency[row_i[1]],labels=c("heterozygotním", "homozygotním"),breaks = c(1,0.8,0.2))
      print(paste("Molekulárně genetickým vyšetřením genu GJB2 byla u pacienta zjištěna přítomnost patogenní varianty",variant[4],"(",variant[5],") v",type,"stavu."))
    } else {
      print("Nebyla detekovaná varianta v GJB2 genu.")
    }
  } else {
    print("Nebyla detekovaná varianta v GJB2 genu.")
  }
}

