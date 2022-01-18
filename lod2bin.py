if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Auctus A6 dumper')
    parser.add_argument('--split', default=False, action="store_true",
                        help='split the memory locations')
    parser.add_argument('--begin', type=lambda x: int(x,0),
                        help='extract the bin beginning at address',
                        default=0x82000000)
    parser.add_argument('-i', '--input', default='/dev/stdin',
                        type=str, help='input lod')
    parser.add_argument('-o', '--out', default='/dev/stdout',
                        type=str, help='output bin')
    parser.add_argument('-v','--verbosity', default=0, action='count',
                        help='print sent and received frames to stderr for debugging')
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s 0.0.1',
                        help='display version information and exit')
    args = parser.parse_args()
    inlod = open(args.input, "r")
    outbin = open(args.out, "wb")
    curaddress = None
    for line in inlod.readlines():
        if line[0] == "#":
            continue
        if line[0] == "@":
            address = int(line[1:], 16)
            if curaddress is None:
                curaddress = address
            elif address != curaddress:
                print("address out of order {} to {}".format(curaddress, address))
            continue
        curaddress += 4
        data = int(line,16)
        outbin.write(data.to_bytes(4, 'little'))
