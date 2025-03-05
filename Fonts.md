# mapnik_xml



Try forcing Mapnik to recognize the font by regenerating the font cache:


```bash
fc-cache -fv

```




```
import mapnik
for font in mapnik.FontEngine.face_names():
    if "DejaVu" in font:
        print(font)
```












It looks like `mapnik.FontEngine.face_names()` is returning an object instead of a list. Try printing it correctly using:  

```python
import mapnik
print(list(mapnik.FontEngine.face_names()))
```

or  

```python
import mapnik
for font in mapnik.FontEngine.face_names():
    print(font)
```

This will show all the fonts Mapnik recognizes. Check if **"DejaVu Serif"** appears in the list. If it’s missing, Mapnik is not detecting the font properly, and you may need to manually add it using:  

```python
import mapnik
mapnik.FontEngine.register_font('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf')
print(list(mapnik.FontEngine.face_names()))
```




