from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import pickle

generate_results = True
read_results = True
results_file = 'results.xml'


if generate_results == True:
    sequence_data = open("gRNAtest.txt").read().split('\n')
    print(sequence_data)
    print('Executing BLAST...')
    result_handle = NCBIWWW.qblast("blastn",
                                      "nr",
                                      sequence_data,
                                      alignments=50,
                                      hitlist_size=2,
                                      entrez_query='Saccharomyces cerevisiae S288C [Organism]')
    print('Done')
    print('Result handle:',result_handle)

    with open(results_file, 'w') as save_file:
        blast_results = result_handle.read()
        save_file.write(blast_results)

    with open(results_file, 'w') as save_file:
        blast_results = result_handle.read()
        save_file.write(blast_results)
# with open("results.xml") as result_handle:
# print(result_handle)

# from Bio.Blast import NCBIXML
# blast_records = NCBIXML.parse(result_handle)

if read_results == True:

    # result_handle=open(results_file)
    blast_records=NCBIXML.parse(result_handle)
    # print(type(blast_records))
    # blast_records=list(blast_records)
    # print(blast_records)

    # for record in blast_records:
    #     print(record)
    # E_VALUE_TRESH=0.5
    for record in blast_records.alignments:
        print(record)
        if record.alignments:
            print("\n")
            print("query: %s" %record.Hsp_qseq[0:100])
            print("match:" %record.hit_id[0:100])
            # for align in record.alignments:
            #     for hsp in align.hsp:
            #         if hsp.expect<E_VALUE_TRESH:
            #             print("matc:%s" %s align.hsptitle[:100])


# for alignment in blast_records.alignments:
#     for hsp in alignment.hsps:
#         if hsp.expect < E_VALUE_TRESH:
#             print('****Alignment****')
#             print('sequence:', alignment.qseq)
#             print(alignment.hit_id[0:100]+'...')
#             print(hsp.qseq[0:75]+'...')
#             print(hsp.match[0:75]+'...')
#             print(hsp.sbject[0:75]+'...')


# for record in NCBIXML.parse(open("results.xml")):
#     if record.alignments:
#         print("\n")
#         print("Hit: %s" % record.Hit_id[:100])
#         for align in record.alignments:
#             for hsp in align.hsps:
#                 if hsp.expect < E_VALUE_TRESH:
#                     print("match: %s " % align.title[:100])
