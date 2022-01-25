# cough-classification
project untuk mendeteksi penyakit melalui suara batuk

## About data
Data coswara dapat diunduh [`disini`](https://github.com/iiscleap/Coswara-Data).
Data diekstrak menggunakan script [`extract_data.py`](https://github.com/iiscleap/Coswara-Data/blob/master/extract_data.py). Script tersebut hanya bisa dijalankan pada OS Linux.
Kemudian data hasil ekstrak dikelompokkan kedalam kategori negatif dan positif serta perbaikan label menggunakan script [`prepocessing-labelling.py`](https://github.com/rjrouf/cough-classification/blob/master/prepocessing-labelling.py)

## how to use?
- Classification dan prepocessing menggunakan data coswara
- model.h5 yang ada adalah model hasil training classification menggunakan data coswara
- untuk menggunakan data lain, ubah parameter `main_dir` pada file [`Prepocessing.ipynb`](https://github.com/rjrouf/cough-classification/blob/master/Prepocessing.ipynb) dengan directory data suara yang akan di proses

## how to test?
- Ubah parameter `filename` pada file [`Testing.ipynb`](https://github.com/rjrouf/cough-classification/blob/master/Testing.ipynb) dengan directory data suara yang akan di tes
