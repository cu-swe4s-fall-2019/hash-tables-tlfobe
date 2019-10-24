import hash_functions
import hash_tables
import matplotlib
import time
import sys
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
    try:
        with open(args.filename, 'r') as f_handle:
            keys = []
            for l in f_handle.readlines():
                keys.append(l.rstrip())
    except IsADirectoryError:
        print("collision_resolution: file selected was not a datafile", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("collision_resolution: please input a valid file path", file=sys.stderr)
        sys.exit(1)

    hash_fxn = eval("hash_functions.h_"+args.hash_fxn)

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

    # Build time to load/search plot

    col_res = eval("hash_tables."+args.col_res)


    N = len(keys)
    if args.col_res == "QuadraticProbe":
        N = int(2*N+1) # Quadratic Probing is not guarenteed to fill the entire array

    hash_table = col_res(hash_fxn, N = N)
    times_to_add = []
    load_factors = []
    for word in keys:
        t0 = time.time()
        hash_table.add(word, word)
        t1 = time.time()
        times_to_add.append(t1 - t0)
        load_factors.append(hash_table.capacity/hash_table.N)

    fig = plt.figure(figsize=(3,3),dpi=300)    
    ax = fig.add_subplot(1,1,1)

    ax.plot(load_factors, times_to_add, '.', ms=1, alpha=0.5)
    ax.set_xlabel("Load Factor")
    ax.set_ylabel("Add Time")
    
    plt.savefig(args.out_id+"_"+args.col_res+"_"+args.hash_fxn+"_add.png", bbox_inches='tight')  

    # Build time to load/search plot

    times_to_search = []
    for word in keys:
        t0 = time.time()
        hash_table.search(word)
        t1 = time.time()
        times_to_search.append(t1 - t0)

    fig = plt.figure(figsize=(3,3),dpi=300)    
    ax = fig.add_subplot(1,1,1)

    ax.plot(list(range(1, len(times_to_search)+1)), times_to_search, '.', ms=1, alpha=0.5)
    ax.set_xlabel("Hashed Word")
    ax.set_ylabel("Search Time")
    
    plt.savefig(args.out_id+"_"+args.col_res+"_"+args.hash_fxn+"_search.png", bbox_inches='tight')  



if __name__ == "__main__":
    main()