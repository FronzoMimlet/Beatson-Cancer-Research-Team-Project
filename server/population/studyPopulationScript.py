import sys
import os
 
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.insert(0, project_root)

import unittest
import json
from application import app

class PopulateStudies(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_populate_studies(self):
        data = {
            "study": { 
                "accession" : "E-MTAB-6620",
                "description": "Recently, we defined four subtypes of pancreatic cancer that are associated with distinct histopathological characteristics and differential survival, namely, Squamous, Pancreatic Progenitor, Immunogenic, and ADEX (Bailey et al 2016, Nature). We also found that loss of CXCR2 was associated with a switch away from the squamous subtype (Steele et al 2016, Cancer Cell). Here we set out to investigate whether inhibition of CSF1R could also result in an alteration of transcriptomic subtype. Pancreatic tumors were harvested from control KPC mice, or mice treated with CSF1R inhibitor (AZD7507) and/or CXCR2 inhibitor (AZD5069) (n≥5). Tissues were stored in RNAl8r at -80C before RNA was prepared, and RNASeq analysis carried out. Reads were analysed using the bcbio-nextgen framework (https://bcbio-nextgen.readthedocs.org/en/latest/). After quality control and adaptor trimming, reads were aligned to the mouse genome build (UCSC mouse mm10) using STAR. Counts for known genes were generated using the function featureCounts in the R/Bioconductor package Rsubread. The R/Bioconductor package edgeR was used to identify differentially expressed genes.",
                "organism": "Mus musculus",
                "study_type":"RNA-seq of coding RNA",
                "publication":"Juliana B Candido, Jennifer P Morton, Peter Bailey, Andrew D Campbell, Saadia A Karim, Thomas Jamieson, Laura Lapienyte, Aarthi Gopinathan, William Clark, Ewan J McGhee, Jun Wang, Monica Escorcio-Correia, Raphael Zollinger, Rozita Roshani, Lisa Drew, Loveena Rishi, Rebecca Arkell, TR Jeffry Evans, Colin Nixon, Duncan I Jodrell, Robert W Wilkinson, Andrew V Biankin, Simon T Barry, Frances R Balkwill, Owen J Sansom.. CSF-1R+ macrophages sustain pancreatic tumorigenesis through T-cell suppression and maintenance of key gene programs that define the squamous subtype"
            }
        }
        response = self.app.post('/create_study', json=data)
        self.assertEqual(response.status_code, 200)
        
   

if __name__ == '__main__':
    print('Starting to populate database...')
    unittest.main()
    print('Database population complete.')