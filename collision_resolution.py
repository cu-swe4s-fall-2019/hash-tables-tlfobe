import hash_functions
import hash_tables
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse

def main():
    parser = argparse.ArgumentParser(description="A program to plot collision"+
                                     " strategies of various hash functions" +
                                     "hash tables",
                                     )
    parser.add_argument('--hash_fxn',
                        type = str,
                        required=True,
                        choices=['ascii', 'rolling', 'FNV'],
                        help="Specific hash function to process keys"
                        )
    parser.add_argument('--col_res',
                        type = str,
                        required=True,
                        choices=["LinearProbe", "QuadraticProbe", "ChainedHash"],
                        help="collision strategy within hashtable"
                        )
    parser.add_argument("--filename",
                        type =str,
                        required=True,
                        help="file to pull keys from"
                        )
    parser.add_argument("--out_id",
                        type= str,
                        required= False,
                        default= "output",
                        help = "name of file to write graphs to"
                        )

    args = parser.parse_args()

    # Read in file to array of keys

    with open(args.filename, 'r') as f_handle:
        keys = []
        for l in f_handle.readlines():
            keys.append(l.rstrip())

    hash_fxn = eval("hash_functions.h_"+args.hash_fxn)
    col_res = eval("hash_tables."+args.col_res)

    # Build subplot based on size of col_resols and hash_fxns
    hash_vals = []
    for word in keys:
        hash_vals.append(hash_fxn(word, len(keys)))
    
    fig = plt.figure(figsize=(3,3),dpi=300)    
    ax = fig.add_subplot(1,1,1)

    ax.plot(list(range(1, len(hash_vals)+1)), hash_vals, '.', ms=1, alpha=0.5)
    ax.set_xlabel("Hashed Word")
    ax.set_ylabel("Hashed Value")

    plt.savefig(args.out_id+"_"+args.hash_fxn+".png", bbox_inches='tight')  





if __name__ == "__main__":
    main()