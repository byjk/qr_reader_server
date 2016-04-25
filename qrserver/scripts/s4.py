#!/usr/bin/python
import sys

def parse_s4_barcode(barcode):
    r = {}
    if barcode.startswith('S4D'):
        a = barcode[3:].split('.')
        r['doc_id'] = int(a[0])
        r['version_id'] = int(a[1])
    elif barcode.startswith('S4A') or barcode.startswith('S4O'):
        a = barcode[3:]
        r['art_id'] = int(a)
    return r
         

if len(sys.argv) > 1:
    barcode = sys.argv[1] 
    # print (barcode)
    r = parse_s4_barcode(barcode)
    print(r)
    
