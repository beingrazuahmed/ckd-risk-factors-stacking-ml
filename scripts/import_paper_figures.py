#!/usr/bin/env python3
"""Prepare browser-friendly CKD figure copies from explicitly approved source images.

Does not assign published figure captions, infer rights, or modify the original inputs.
Source files are *not* copied into the project without a separate rights review.
"""
from pathlib import Path
from PIL import Image, ImageOps
import argparse


def main():
    parser=argparse.ArgumentParser(description='Convert supplied CKD research figures to web PNG previews')
    parser.add_argument('source',type=Path,help='Folder containing authorized TIFF/PNG publication figure files')
    parser.add_argument('--out',type=Path,default=Path('figures/previews'),help='Output directory for web figures')
    parser.add_argument('--max-width',type=int,default=1800)
    args=parser.parse_args()
    if args.max_width<500:raise SystemExit('Choose a reasonable max-width >= 500 px')
    if not args.source.is_dir():raise SystemExit(f'Input directory not found: {args.source}')
    paths=sorted(p for p in args.source.iterdir() if p.is_file() and p.suffix.lower() in {'.tif','.tiff','.png'})
    if not paths:raise SystemExit('No TIFF/PNG images found in that folder')
    args.out.mkdir(parents=True,exist_ok=True)
    for idx,source in enumerate(paths,1):
        with Image.open(source) as im:
            im=ImageOps.exif_transpose(im)
            im.load()
            if im.mode not in ('RGB','RGBA'):im=im.convert('RGB')
            if im.width>args.max_width:
                im.thumbnail((args.max_width,99999),Image.Resampling.LANCZOS)
            # Keep a filename trace back to its actual source; do not invent figure numbering.
            safe=''.join(c.lower() if c.isalnum() else '-' for c in source.stem).strip('-')
            dst=args.out/f'{safe}.png'
            if dst.exists():raise SystemExit(f'Refusing to overwrite existing figure: {dst}')
            im.save(dst,format='PNG',optimize=True)
            print(f'{source.name} -> {dst} [{im.width}x{im.height}]')
    print('Review images, captions, accuracy, attribution and licensing before GitHub publication.')

if __name__=='__main__':main()
