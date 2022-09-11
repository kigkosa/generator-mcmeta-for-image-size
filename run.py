import os
import cv2

for file in os.listdir('textures'):
    for file2 in os.listdir('textures/' + file):
        # shutil.copy('textures/'+file+'/' + file2,'textures/'+file+'/' + file2.replace('.png','_e.png'))
        im = cv2.imread('textures/'+file+'/' + file2)
        h, w, c = im.shape
        if h != w:
            i = int(h/ w)
            print(i)
            # for x in range(i):
            #     print(x)
            with open(f"textures/{file}/{file2}.mcmeta", "w") as f:
                f.write(f'{{')
                f.write(f'\n\t"animation": {{')
                f.write(f'\n\t"frametime": 5,')
                f.write(f'\n\t"frames": [')
                for x in range(i):
                    f.write(f'\n\t\t{x}')
                    if x != i-1:
                        f.write(f',')
                f.write(f'\n\t]')
                f.write(f"\n  }}")
                f.write(f"\n}}")

