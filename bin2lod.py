if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Auctus A6 dumper')
    parser.add_argument('--begin', type=lambda x: int(x,0),
                        help='extract the bin beginning at address',
                        default=0x08000000)
    parser.add_argument('-i', '--input', default='/dev/stdin',
                        type=str, help='input bin')
    parser.add_argument('-o', '--out', default='/dev/stdout',
                        type=str, help='output lod')
    parser.add_argument('-v','--verbosity', default=0, action='count',
                        help='print sent and received frames to stderr for debugging')
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s 0.0.1',
                        help='display version information and exit')
    args = parser.parse_args()

    sector_size = 0x1000
    sector = 0
    curaddress = args.begin
    with open(args.input, "rb") as inbin, open(args.out, "w") as outlod:
        word = inbin.read(4)
        while word:
            if sector == 0:
                outlod.write("@%08x\n" % curaddress)
                sector = sector_size - 4
            else:
                sector -= 4
            curaddress += 4
            outlod.write("%08x\n" % int.from_bytes(word, byteorder='little'))
            word = inbin.read(4)
