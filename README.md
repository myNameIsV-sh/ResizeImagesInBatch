# ResizeImagesInBatch
Redimensione imagens em lotes, usando o seu computador e sem depender de terceiros.

## Sumário
- [Como surgiu?](#como-surgiu)
- [Por que Python?](#por-que-python)
- [Como utilizar](#como-utilizar)

## Como surgiu?
Sou um fotógrafo no meu tempo livre e, ao final das sessões, depois que todas as fotos são escolhidas, é preciso redimensioná-las para publicá-las em seguida. Esse processo acaba sendo bem chato e repetitivo, se tornando ainda mais quando é preciso exportar para outras proporções.

Em um fim de semana com a minha namorada, essa necessidade se mostrou presente e eu decidi escrever esse _script._

## Por que Python?
Python não é a minha linguagem principal, mas eu estava com preguiça e precisava resolver essa situação o quanto antes, optei pelo Python por conta da disponibilidade de bibliotecas e pela sua simplicidade.

## Como utilizar
Antes de executar o _script_ rode o comando:

```
pip install pillow
```

Em seguida, defina os parâmetros de entrada e de saída, `input_folder` é a pasta que contém todas as imagens, `output_folder` é a pasta que será criada ao fim do processo; recomendo utilizar _Raw Strings_ para evitar erros na hora de acessar os endereços.

```
# Windows
input_folder = r"C:\Users\YourUser\Pictures\ImagesToResize"
output_folder = r"C:\Users\YourUser\Pictures\ResizedImages"

# Linux
input_folder = "/home/your_user/Pictures/ImagesToResize"
output_folder = "/home/your_user/Pictures/ResizedImages"
```

Defina também a resolução desejada (altura e largura).

```
height, width = 1920, 1080
```

Talvez seja necessário ajustar alguns parâmetros caso as suas imagens possuam uma extensão diferente (prometo que irei ajustar isso)

```
if file.lower().endswith(".jpg", ".png", ".etc"):
```

Também pode ser interessante ajustar a qualidade do redimensionamento

```
img_resized.save(out_path, quality=95)
```

Feito esses pequenos ajustes, basta executar o _script_ e procurar as imagens redimensionadas :)
