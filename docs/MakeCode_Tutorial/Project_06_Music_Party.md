### Progetto 06: Festa Musicale

![Img](./media/A1317.png)

#### 1. Panoramica

Quando battiamo le mani, il microfono sulla scheda rileva i segnali sonori, e l'altoparlante riproduce una allegra canzone di compleanno mentre il LED RGB emette una luce abbagliante.

#### 2. Componenti

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| scheda micro:bit *1 | scheda di espansione micro:bit tipo T *1 | cavo micro USB *1 |
| ![Img](./media/A500.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| LED rosso *1 | resistore 220Ω *3 | filo jumper *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A621.png)  |
| breadboard *1 | portabatterie *1 <br> (<span style="color: rgb(255, 76, 65);">batterie AA auto-fornite *2</span>)| scheda RGB *1 |

#### 3. Conoscenza dei Componenti

**Microfono**

Un microfono digitale di alta qualità è integrato sul lato frontale della scheda micro:bit V2 per rilevare segnali sonori e audio. Il chip che controlla e processa il microfono si trova sul retro.

![Img](./media/A1317.png)

Il microfono è in un piccolo foro rotondo sulla parte frontale della scheda, comodo per catturare i segnali sonori circostanti. Basta posizionare la scheda micro:bit con il lato frontale rivolto verso l'alto durante l'uso. Accanto al foro c'è un indicatore LED del microfono. Quando il micro:bit misura i livelli sonori, l'indicatore si accende.

![Img](./media/A116.png)

**LED RGB**

![Img](./media/A2127.png)

Il LED RGB è rappresentato dall'intersezione di tre colori primari (RGB): rosso, verde e blu. La maggior parte dei colori può essere sintetizzata da RGB in proporzioni diverse. I LED rosso, verde e blu sono racchiusi in un involucro di plastica trasparente per emettere colori di luce variando la tensione di ingresso dei pin R, G e B.

![Img](./media/A137.png)

**Teoria tricromatica:**

![Img](./media/A150.png)

Il LED RGB può essere diviso in due tipi: anodo comune e catodo comune:

In un LED RGB a catodo comune, i tre LED condividono una connessione negativa (catodo);

In un LED RGB ad anodo comune, i tre LED condividono una connessione positiva (anodo).

![Img](./media/A209.png)

<span style="color: rgb(255, 76, 65);">**Nota: Qui forniamo un LED RGB a catodo comune.**</span>

**Pin del LED RGB:**

Il LED RGB ha 4 pin: GND (il più lungo), R (rosso), G (verde) e B (blu). Posizionare il LED RGB come mostrato sotto, i pin da sinistra a destra sono rosso, GND, verde e blu.

![Img](./media/A239.png)

#### 4. Schema di Collegamento

![Img](./media/A308.png)

![Img](./media/A325.png)

#### 5. Flusso del Codice

![Img](./media/A343.png)

#### 6. Codice di Test

Il file del codice è fornito nella cartella Progetto 06：Festa Musicale, file Project-06-Music-Party.hex.

![Img](./media/A423.png)

**Carica i blocchi di codice:**

![Img](./media/A445.png)

#### 7. Risultato del Test

Dopo aver scaricato il codice sulla scheda, quando battiamo le mani, il microfono sulla scheda rileva i segnali sonori, e l'altoparlante riproduce una allegra canzone di compleanno mentre il LED RGB emette una luce abbagliante. Non è forse la festa musicale in un'atmosfera felice e gioiosa?

<span style="color: rgb(255, 76, 65);">**ATTENZIONE:** Se il collegamento è corretto ma non si vedono i risultati, premere il pulsante di reset sul retro della scheda.</span>

![Img](./media/A757.gif)
