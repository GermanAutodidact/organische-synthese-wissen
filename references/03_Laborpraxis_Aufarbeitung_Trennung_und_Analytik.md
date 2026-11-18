# 03 – Laborpraxis, Aufarbeitung (`Workup`), Trennverfahren & Instrumentelle Analytik

Dieses Modul überträgt sämtliche praktischen Methoden, Daten-Tabellen, Rezepturen, Sicherheitsgesetze und Troubleshooting-Protokolle aus Lisa Nichols' *Organic Chemistry Lab Techniques* (`libretexts_lab_techniques`, 162 Kapitel), den Synthese- und Strukturvalidierungs-Regelwerken von `codex-organic-chem` sowie den Prozess-, Analytik- und Spektroskopie-Modulen von `scientific-agents` und `scientific-agent-skills` (`nmrglue`, `matchms`, `pyopenms`) in ein verlustfreies deutsches Laborhandbuch.

---

<!-- TOC_START -->
## Inhaltsverzeichnis & Zeilen-Index

| Abschnitt | Ebene | Zeilen |
| :--- | :--- | :---: |
| [1. Reaktionsführung, Apparatur-Praxis & Schutzgastechnik](#sec-1) | Hauptabschnitt | Z. 37–38 |
| ↳ [1.1 Glasgeräte, Schliffe, Fetten & Proben-Transfer](#sec-2) | Unterabschnitt | Z. 40–54 |
| ↳ [1.2 Kühlbäder (`Cooling Baths`): Vollständige Temperatur-Referenz ($0\,^\circ\text{C}$ bis $-196\,^\circ\text{C}$)](#sec-3) | Unterabschnitt | Z. 56–81 |
| ↳ [1.3 Heizmethoden, Rückfluss (`Reflux`), Tropftrichter & Inertgas-Technik](#sec-4) | Unterabschnitt | Z. 83–106 |
| [2. Die Quench- & Aufarbeitungs-Kaskade (`Workup`)](#sec-5) | Hauptabschnitt | Z. 108–109 |
| ↳ [2.1 Gezieltes Quenchen überschüssiger Reagenzien (Reagenz-spezifische Quench-Matrix)](#sec-6) | Unterabschnitt | Z. 111–132 |
| ↳ [2.2 Flüssig-Flüssig-Extraktion: Verteilungsgesetz, Phasenbestimmung & Säure-Base-Trennungs-Kaskade](#sec-7) | Unterabschnitt | Z. 134–172 |
| ↳ [2.3 Praktische Problemlösung im Scheidetrichter: Emulsionen, Brine, Trocknungsmittel & Rotationsverdampfer](#sec-8) | Unterabschnitt | Z. 174–208 |
| [3. Reinigungsverfahren: Umkristallisation, Destillation, Sublimation & Chromatographie](#sec-9) | Hauptabschnitt | Z. 210–211 |
| ↳ [3.1 Umkristallisation (`Crystallization`, LibreTexts Kapitel 3)](#sec-10) | Unterabschnitt | Z. 213–231 |
| ↳ [3.2 Destillation & Sublimation (LibreTexts Kapitel 5 & 6.03)](#sec-11) | Unterabschnitt | Z. 233–256 |
| ↳ [3.3 Dünnschichtchromatographie (`DC`/`TLC`), Anfärbereagenzien & Säulenchromatographie](#sec-12) | Unterabschnitt | Z. 258–298 |
| ↳ [3.4 Gaschromatographie (`GC`), Chirale HPLC/SFC & Prozess-Kristallisation (`Scale-up`)](#sec-13) | Unterabschnitt | Z. 300–322 |
| [4. Analytik, Nasschemische Nachweise & Instrumentelle Strukturaufklärung](#sec-14) | Hauptabschnitt | Z. 324–325 |
| ↳ [4.1 Schmelzpunkt (`mp`), Mischschmelzpunkt & Klassische Nasschemische Nachweise (LibreTexts Kapitel 6)](#sec-15) | Unterabschnitt | Z. 327–354 |
| ↳ [4.2 Infrarot- (`IR`) & Raman-Spektroskopie (inkl. Spektroskopie-Praxisregeln)](#sec-16) | Unterabschnitt | Z. 356–389 |
| ↳ [4.3 $^1\text{H}$- und $^{13}\text{C}$-NMR-Spektroskopie, Restlösungsmittel & `nmrglue`-Prozessierung](#sec-17) | Unterabschnitt | Z. 391–434 |
| ↳ [4.4 Massenspektrometrie (`MS`, `HRMS`, `MS/MS`), Fragmentierung, `matchms`/`pyOpenMS` & Methodenvalidierung](#sec-18) | Unterabschnitt | Z. 436–476 |
| ↳ [4.5 Organometall-, Photoredox- & Elektrochemische Charakterisierung (`organometallic-chemist`, `photochemist`, `electrochemist`)](#sec-19) | Unterabschnitt | Z. 478–490 |

---

<!-- TOC_END -->

<a id="sec-1"></a>
## 1. Reaktionsführung, Apparatur-Praxis & Schutzgastechnik

<a id="sec-2"></a>
### 1.1 Glasgeräte, Schliffe, Fetten & Proben-Transfer

1. **Schliffe (`Ground Glass Joints`) & Schlifffett:**
   - Normschliffe (z. B. `NS 14/23`, `NS 29/32`) dicht halten durch **hauchdünnes** Einfetten nur im oberen Drittel des Kerns mit Silikon- oder Krytox-/PTFE-Fett (oder Verwendung von PTFE-Manschetten). **Nie zu viel Fett** verwenden $\rightarrow$ sonst Verunreinigung des Produkts im $^1\text{H}$-NMR (berüchtigter Silikonfett-Singulett-Peak bei **$\delta = 0.07\text{ ppm}$ in $\text{CDCl}_3$**!).
   - **Verbot von Fett bei stark basischen / fluoridhaltigen Reaktionen:** Starke Basen ($\text{NaOH}$, $\text{KOH}$, $\text{KO}t\text{Bu}$, $\text{NaH}$) greifen Glasoberflächen an und verbacken Schliffe unlösbar (**„Einfrieren“**); PTFE-Hülsen verwenden! Bei Destillationen unter Vakuum niemals einen ungefetteten Schliff unter Hitze stehen lassen.
   - **Schliffklammern (`Keck Clips`):** Nie auf stark erhitzten Schliffen verwenden (schmelzen bei $>140\,^\circ\text{C}$ $\rightarrow$ Drahtklammern/Federn nutzen!); das breitere Ende der Keck-Klammer gehört stets auf die Hülse (`Female Joint`), das schmalere um den Kern (`Male Joint`).
2. **Transfer von Flüssigkeiten & Feststoffen:**
   - **Reaktionsansatz-Regel:** Niemals Feststoffe durch einen schmalen Schliff schütten, ohne ihn danach mit trockenem Lösungsmittel nachzuspülen; sonst bleibt Edukt im Schliff kleben (verfälscht Stöchiometrie und lässt Schliffe fressen).
   - **Kalibrierte Glaspipetten & Spritzen:** Luftempfindliche und pyrophore Flüssigkeiten ($\text{RLi}$, $\text{RMgX}$, $\text{DIBAL-H}$, $\text{BH}_3\cdot\text{THF}$, $\text{TiCl}_4$) ausschließlich über **Septa** mit Stickstoff-gespülten Spritzen/Kanülen oder per **Kanülen-Transfer (`Cannula Transfer`)** unter leichtem Argon-/$\text{N}_2$-Überdruck abmessen und transferieren.
3. **Trocknen von Glasgeräten (`Oven-Drying` vs. `Flame-Drying`):**
   - **Trockenschrank:** Mindestens $4\text{--}12\text{ h}$ bei $120\text{--}140\,^\circ\text{C}$ (Septa, Kunststoffteile, geeichte Volumenmesskolben und Rührfische **nicht** in den heißen Ofen legen!), heiß entnehmen, sofort mit trockenem Septum verschließen und unter **Argon/$\text{N}_2$-Strom** auf RT abkühlen lassen.
   - **Ausflammen (`Flame-Drying`):** Apparatur im **Vakuum** ($<1\text{ mbar}$) montieren, mit dem Bunsenbrenner oder Heißluftfön von unten nach oben abflammen (um Feuchtigkeit als sichtbaren Beschlag auszutreiben und zu verhindern, dass sie am kühlen oberen Teil wieder kondensiert!), anschließend mit trockenem Argon/$\text{N}_2$ fluten (3 Zyklen **`Evacuate-Backfill`**). **STRIKTES VERBOT:** Niemals ausflammen, solange leicht entzündliche Lösungsmittel ($\text{Et}_2\text{O}$, Hexan, $\text{THF}$, Aceton) in der Nähe stehen!

---

<a id="sec-3"></a>
### 1.2 Kühlbäder (`Cooling Baths`): Vollständige Temperatur-Referenz ($0\,^\circ\text{C}$ bis $-196\,^\circ\text{C}$)

> **Labor-Regeln für Kühlbäder (LibreTexts 1.4J):**
> - Für Bäder **kälter als $-10\,^\circ\text{C}$** zwingend ein **isoliertes Dewar-Gefäß** (mit Schutznetz/Kunststoffummantelung gegen Implosion!) verwenden, kein offenes Becherglas (sonst schlägt sich Luftfeuchtigkeit als Eis nieder und das Bad erwärmt sich zu schnell).
> - **Trockeneis-Zugabe:** Trockeneis ($\text{CO}_2\text{(s)}$, Sublimationspunkt $-78.5\,^\circ\text{C}$) **immer langsam in kleinen Stücken** zum vorgekühlten Lösungsmittel (Aceton, Isopropanol, $\text{MeCN}$, $\text{CHCl}_3$, $\text{MeOH}$) geben – bei zu schneller Zugabe schäumt die Lösung durch heftige $\text{CO}_2$-Gasentwicklung über! Temperaturen unterhalb von $-78\,^\circ\text{C}$ erfordern zwingend **flüssigen Stickstoff ($\text{N}_2\text{(fl.)}$)** als Kälteträger.
> - **Sicherheit:** Niemals Trockeneis oder Bäder $<-10\,^\circ\text{C}$ mit bloßen Händen berühren (**schwere Kälteverbrennungen / Erfrierungen!**). Bei Verwendung von **flüssigem Stickstoff ($\text{N}_2\text{(fl.)}, -196\,^\circ\text{C}$)** niemals offene Gefäße mit Luftzutritt lange tiefkühlen, da **flüssiger Sauerstoff ($\text{bp } -183\,^\circ\text{C}$, blassblau!)** aus der Luft einkondensiert und mit organischen Lösungsmitteln extrem explosive Gemische bildet!

| Bad-Zusammensetzung (Mischungsverhältnis pro $100\text{ g}$ Eis bzw. Lösungsmittel) | Erzielte Zieltemperatur ($^\circ\text{C}$) | Typische Synthese-Anwendung |
| :--- | :---: | :--- |
| **Eis / Wasser-Slurry** ($1:1$ mit Wasser bedeckt!) | **$0\,^\circ\text{C}$** | Mildes Quenchen, Diazotierungen, Ester-Verseifung, $\text{NaBH}_4$-Reduktion |
| **$75\text{ g NaNO}_3 + 100\text{ g}$ zerstoßenes Eis** | **$-5.3\,^\circ\text{C}$** | Diazotierung empfindlicher Aniline |
| **$33\text{ g NaCl} + 100\text{ g}$ zerstoßenes Eis** (Eutektikum) | **$-15\text{ bis }-21\,^\circ\text{C}$** | Milde Oxidationen, Azid-Bildungen, Kühlung von Rückflusskühlern bei leichtflüchtigen Stoffen |
| **$66\text{ g NaBr} + 100\text{ g}$ zerstoßenes Eis** | **$-28\,^\circ\text{C}$** | Sharpless Asymmetrische Epoxidierung ($-20\,^\circ\text{C}$), Corey-Kim ($-25\,^\circ\text{C}$) |
| **$125\text{ g CaCl}_2\cdot 6\text{H}_2\text{O} + 100\text{ g}$ zerstoßenes Eis** | **$-40\text{ bis }-50\,^\circ\text{C}$** | Kryoreaktionen ohne Trockeneis |
| **Acetonitril ($\text{MeCN}$) + Trockeneis ($\text{CO}_2\text{(s)}$)** | **$-40\,^\circ\text{C}$** | Kinetische Deprotonierungen, Grignard-Halogen-Metall-Austausch ($i\text{-PrMgCl}\cdot\text{LiCl}$) |
| **Chloroform ($\text{CHCl}_3$) + Trockeneis** *(im Abzug!)* | **$-61\,^\circ\text{C}$** | Kinetische Enolisierungen |
| **Methanol ($\text{MeOH}$) + Trockeneis ($\text{CO}_2\text{(s)}$)** | **$-72\,^\circ\text{C}$** | Alternative zu Aceton/Trockeneis; Achtung bei Feuchtigkeit: $\text{MeOH}$ ist hygroskopisch |
| **Aceton oder Isopropanol + Trockeneis ($\text{CO}_2\text{(s)}$)** | **$-78\,^\circ\text{C}$** | **Standard-Kryobad!** $\text{LDA}$, $n\text{-BuLi}/t\text{-BuLi}$, $\text{DIBAL-H}$, Swern-Oxidation, Ozonolyse, Ireland-Claisen |
| **Ethylacetat ($\text{EtOAc}$) + flüssiger Stickstoff ($\text{N}_2\text{(fl.)}$, Slush)** | **$-84\,^\circ\text{C}$** | Extrem selektiver Halogen-Lithium-Austausch *(mit Trockeneis physikalisch nicht unter $-78{,}5\,^\circ\text{C}$ kühlbar!)* |
| **$n$-Hexan + flüssiger Stickstoff ($\text{N}_2\text{(fl.)}$, Slush)** | **$-94\text{ bis }-95\,^\circ\text{C}$** | Hochselektive Enolat-/Carbenoid-Bildungen ($\text{LiCH}_2\text{Cl}$!) |
| **Methanol ($\text{MeOH}$) + flüssiger Stickstoff ($\text{N}_2\text{(fl.)}$, Slush)** *(Achtung: zähflüssig!)* | **$-98\,^\circ\text{C}$** | Instabile Organolithium-Spezies (z. B. $\alpha$-Halogenalkyllithium bei $-100\,^\circ\text{C}$) |
| **Diethylether ($\text{Et}_2\text{O}$) + flüssiger Stickstoff ($\text{N}_2\text{(fl.)}$)** | **$-116\,^\circ\text{C}$** | Extrem instabile Carbenoide; **Freeze-Pump-Thaw** von $\text{THF}/\text{Et}_2\text{O}$ |
| **Flüssiger Stickstoff ($\text{N}_2\text{(fl.)}$)** | **$-196\,^\circ\text{C}$** | **Freeze-Pump-Thaw-Entgasen**, Kühlfallen (`Cold Traps`) an Vakuumpumpen und Schlenk-Linien |

---

<a id="sec-4"></a>
### 1.3 Heizmethoden, Rückfluss (`Reflux`), Tropftrichter & Inertgas-Technik

1. **Heizquellen-Auswahl & Brandvermeidung (LibreTexts 1.4A–1.4I):**
   - **Heizblock (Metall-/Aluminiumblock wie *DrySyn* / *Pie-Blocks*) auf Magnetrührer-Heizplatte:** Sauberste, sicherste Standardmethode im modernen Syntheselabor (kein heißes Öl, keine Ölverschmutzung am Kolben, gleichmäßige Wärmeübertragung bis $>200\,^\circ\text{C}$ mit externem Temperaturfühler!).
   - **Wasserbad ($<100\,^\circ\text{C}$):** Sicher für $\text{Et}_2\text{O}$ ($\text{bp } 35\,^\circ\text{C}$), $\text{DCM}$ ($\text{bp } 40\,^\circ\text{C}$), Aceton ($\text{bp } 56\,^\circ\text{C}$), $\text{MeOH}$ ($\text{bp } 65\,^\circ\text{C}$), Hexan ($\text{bp } 69\,^\circ\text{C}$).
   - **Ölbad (Silikonöl bis $\sim 180\text{--}220\,^\circ\text{C}$; darüber Rauch-/Brandgefahr!) & Sandbad ($>200\,^\circ\text{C}$, aber träge Temperaturregelung!):** **Kritische Sicherheitsregel:** Niemals Wasser in heißes Silikonöl ($>100\,^\circ\text{C}$) tropfen lassen (explosives Spritzen!). Kolbenboden sollte maximal bis zur Hälfte eintauchen; immer ein **Sicherheits-Temperaturbegrenzer** (`Contact Thermometer`) einsetzen!
   - **Heizpilz (`Heating Mantle`):** Nur passgenau zur Kolbengröße und immer über Regeltrafo/Temperaturregler betreiben (niemals direkt in die Steckdose!). Für kleine Kolben ($<50\text{ mL}$) ungeeignet; Sand/Alu-Blöcke bevorzugen.
   - **Offene Heizplatte direkt unter Glaskolben:** **STRIKT VERBOTEN** bei niedrig-siedenden, brennbaren Lösungsmitteln ($\text{Et}_2\text{O}$ hat eine Zündtemperatur von nur **$160\,^\circ\text{C}$** – entzündet sich auf einer heißen Keramikplatte ohne jeden Funken!).
   - **Labor-Hebebühne (`Lab Jack`):** Heizquelle immer auf einer Hebebühne platzieren (nicht den Reaktionskolben bewegen!), damit die Hitze bei beginnendem Durchgehen der Reaktion (`Thermal Runaway`) oder Siedeverzug innerhalb von $2\text{ Sekunden}$ abgesenkt werden kann!
2. **Kontrolliertes Sieden & Rückfluss (`Reflux`, LibreTexts 1.4B & 1.4K):**
   - **Kolbenfüllgrad:** Reaktions- oder Destillationskolben **maximal zu $50\,\%$ (ideal $1/3\text{ bis }1/2$)** füllen! Bei $>2/3$ droht Überschäumen in den Kühler.
   - **Siedesteine vs. Magnetrührfisch:** Bei normalem Druck verhindern **Magnetrührfisch** (bei konstanter Rührung) oder **Siedesteine (`Boiling Chips`)** Siedeverzug (`Bumping`). **GOLDENE REGEL:** **Niemals** einen Siedestein in eine bereits heiße oder siedende Flüssigkeit werfen (sofortiges explosionsartiges Aufschäumen/Überkochen!). Bei **Vakuumdestillationen** sind Siedesteine wirkungslos (verlieren die eingeschlossene Luft sofort) $\rightarrow$ zwingend kräftig rühren oder feine Luft-/Inertgas-Siedekapillare verwenden!
   - **Rückflusskühlung (`Reflux`):** Wasser tritt am Kühler **unten** ein und **oben** aus (Gegenstromprinzip und vollständige Füllung des Kühlmantels!). Bei wasserfreien Reaktionen oben auf den Kühler ein **Trockenrohr** ($\text{CaCl}_2$) oder einen **Argon-/$\text{N}_2$-Ballon / Öl-Blasenzähler** setzen – **NIEMALS einen geschlossenen Glasstopfen auf den Rückflusskühler setzen (Überdruck-Explosionsgefahr!)**.
   - **Kondensations-Höhe im Kühler:** Die Heizleistung so einstellen, dass der Kondensationsring der Lösungsmitteldämpfe maximal im **unteren Drittel** des Kühlers bleibt (steigt er höher, entweicht Lösungsmittel!).
3. **Kontrolle exothermer Reaktionen (`Tropftrichter-Regel`):**
   - Exotherme Reaktionen (Grignard-Bildung, $\text{LiAlH}_4$-Reduktion, Nitrierungen, Säurechlorid-Zugaben, $\text{AlCl}_3$-Acylierungen) **niemals alle Reagenzien auf einmal vorlegen** (`All-in Batch` = Thermal-Runaway-Gefahr!).
   - Stattdessen **Druckausgleichs-Tropftrichter (`Addition Funnel`)** einsetzen und die Zugaberate so steuern, dass die interne Reaktionstemperatur (oder ein moderater Rückfluss) kontrolliert bleibt, wobei ein Eis-/Kühlbad auf einer Hebebühne bereitsteht.
4. **Inertgas- & Schlenk-Technik ($\text{N}_2$ vs. Argon, LibreTexts 1.3C & 7.03):**
   - **Argon ($\text{Ar}$, $M = 39.95\text{ g/mol}$) vs. Stickstoff ($\text{N}_2$, $M = 28.01\text{ g/mol}$):** Argon ist **$1.38$-mal schwerer als Luft ($28.97\text{ g/mol}$)** und legt sich als schützende Decke über geöffnete Reaktionskolben; zudem reagiert $\text{N}_2$ mit metallischem **Lithium** bei RT langsam zu $\text{Li}_3\text{N}$ $\rightarrow$ für Lithium-Metall- und sehr empfindliche Katalysereaktionen bevorzugt **Argon** verwenden!
   - **Schlenk-Protokoll (`3× Evacuate-Backfill`):** Kolben an der Schlenk-Linie $3\times$ abwechseln auf $<0.5\text{ mbar}$ evakuieren und mit trockenem Argon/$\text{N}_2$ über einen Quecksilber-/Silikonöl-Blasenzähler belüften. Bei Zugabe fester Reagenzien unter Gegenstrom (`Positive Pressure`) arbeiten.
   - **`Freeze-Pump-Thaw`-Entgasen (Goldstandard zur $\text{O}_2$-Entfernung für Sonogashira, Metathese, Photoredox):** 1. Lösung im Schlenk-Kolben in flüssigem $\text{N}_2$ ($-196\,^\circ\text{C}$) komplett einfrieren. 2. Ventil zur Vakuumpumpe für $5\text{ min}$ öffnen, um den Gasraum abzupumpen. 3. Ventil schließen und Kolben im Wasserbad vollständig auftauen lassen (gelöste Gase blubbern aus!). 4. Mindestens **3 Zyklen** wiederholen, danach mit Argon fluten. *(Alternative für stabile Lösungsmittel: $30\text{ min}$ kräftiges Durchleiten von Argon durch eine Kanüle mit Entlüftungskanüle = `Sparging`).*

---

<a id="sec-5"></a>
## 2. Die Quench- & Aufarbeitungs-Kaskade (`Workup`)

<a id="sec-6"></a>
### 2.1 Gezieltes Quenchen überschüssiger Reagenzien (Reagenz-spezifische Quench-Matrix)

> **Oberstes Quench-Gesetz:** **Vor jeder Aufarbeitung im Scheidetrichter** müssen reaktive, wasserempfindliche, pyrophore oder stark oxidierende Reagenzüberschüsse bei **Kühlung ($0\,^\circ\text{C}$ oder $-78\,^\circ\text{C}$)** kontrolliert vernichtet werden! Ein ungelöschtes Reagenz im Scheidetrichter erzeugt explosionsartigen Überdruck (Stopfen fliegt heraus, Inhalt spritzt ins Gesicht!) oder zerstört das Produkt.

| Verwendetes Reagenz | Sicheres Standard-Quench-Protokoll (Reihenfolge & Temperatur!) | Chemischer Hintergrund & Kritische Fehlerquellen |
| :--- | :--- | :--- |
| **$\text{LiAlH}_4$ (`LAH`)** | Verdünnen mit $\text{Et}_2\text{O}$/$\text{THF}$, auf **$0\,^\circ\text{C}$** kühlen, **Fieser-Workup (`1-1-3`)**: Pro $X\text{ g LAH}$ extrem langsam zutropfen: 1. $X\text{ mL H}_2\text{O}$, 2. $X\text{ mL } 15\,\%\text{ NaOH}$, 3. $3X\text{ mL H}_2\text{O}$ (oder Quench mit $\text{EtOAc}$ dann ges. Rochelle-Salz). | Direkte Säurezugabe erzeugt gelatinösen $\text{Al(OH)}_3$-Schlamm und explosive $\text{H}_2$-Entwicklung! |
| **$\text{NaBH}_4$ / $\text{LiBH}_4$** | Bei **$0\,^\circ\text{C}$** vorsichtig mit **ges. $\text{NH}_4\text{Cl}$-Lösung** oder Aceton/MeOH + verd. $\text{HCl}$ ($\text{pH } 4\text{--}5$) oder verd. Essigsäure quenchen, bis die $\text{H}_2$-Entwicklung stoppt. | Bei $\text{NaBH}_3\text{CN}$ **NIEMALS stark sauer quenchen** ($\rightarrow \text{HCN}\uparrow$!), sondern alkalisch ($\text{NaHCO}_3/\text{NaOH}$)! |
| **$\text{DIBAL-H}$ / $\text{AlMe}_3$ / $\text{Et}_2\text{AlCl}$** | Bei **$-78\,^\circ\text{C}$** (oder $0\,^\circ\text{C}$) mit $\text{MeOH}$ oder $\text{EtOAc}$ quenchen, dann Zugabe eines gleichen Volumens **ges. Kaliumnatriumtartrat-Lösung (Rochelle-Salz)** und **$1\text{--}3\text{ h}$ bei RT kräftig rühren**, bis zwei klare Phasen entstehen! | Ohne Tartrat bildet sich eine undurchdringliche Aluminiumhydroxid-Emulsion, die das gesamte Produkt einschließt. |
| **$\text{NaH}$ / $\text{KH}$** | Bei **$0\,^\circ\text{C}$** unter $\text{N}_2$/Argon zuerst mit **$\text{EtOAc}$** oder langsam tropfenweise mit **$i\text{-PrOH}$** oder **ges. $\text{NH}_4\text{Cl}$-Lösung** quenchen (Vorsicht bei $\text{KH}$: niemals auf einmal Wasser zugeben $\rightarrow$ Selbstentzündung von $\text{H}_2$!). | $\text{NaH}$-Dispersion in Mineralöl hinterlässt Alkan-Signale ($\delta = 0.85, 1.25\text{ ppm}$) $\rightarrow$ per Pentan-Filtration vor dem Ansatz oder Säulenchromatographie entfernen. |
| **$n\text{-BuLi}, t\text{-BuLi}, \text{LDA}, \text{RMgX}$** | Bei **$-78\,^\circ\text{C}$ oder $0\,^\circ\text{C}$** langsam mit **ges. wässriger $\text{NH}_4\text{Cl}$-Lösung** oder (für säureempfindliche Gruppen wie Acetale/Silylester!) mit **wässrigem $\text{pH 7}$-Phosphatpuffer** bzw. trockenem Eis/$\text{MeOH}$ quenchen. | Bei $t\text{-BuLi}$-Resten in Spritzen: Kanüle in Hexan/Isopropanol eintauchen und langsam einsaugen, **nicht** sofort in Wasser halten! |
| **$\text{R}_2\text{CuLi}$ (Organocuprate)** | Bei $-78\,^\circ\text{C} \rightarrow 0\,^\circ\text{C}$ mit einer **9:1-Mischung aus ges. $\text{NH}_4\text{Cl}$ und konz. $\text{NH}_3\text{(aq)}$** quenchen und $30\text{ min}$ an Luft kräftig rühren. | $\text{NH}_3$ oxidiert und komplexiert unlösliche $\text{Cu(I)}$-Salze zu tiefblauem, wasserlöslichem $[\text{Cu(NH}_3)_4]^{2+}$. |
| **$\text{BH}_3$ / Hydroborierung** | Bei $0\,^\circ\text{C}$ tropfenweise $\text{H}_2\text{O}$ (vorsichtig, $\text{H}_2\uparrow$!), dann **$3\,\text{M NaOH}$** + **$30\,\%\,\text{H}_2\text{O}_2$** ($1:1$ langsam zutropfen, stark exotherm!), $1\text{ h}$ bei RT–$50\,^\circ\text{C}$ rühren; Restperoxide mit $\text{Na}_2\text{S}_2\text{O}_3$ vernichten! | Bei säureempfindlichen Substraten statt $\text{NaOH}/\text{H}_2\text{O}_2$ das milde **$\text{NaBO}_3\cdot 4\text{H}_2\text{O}$** (Natriumperborat in $\text{THF}/\text{H}_2\text{O}$) verwenden! |
| **Persäuren ($m\text{CPBA}$), $\text{O}_3$, $\text{TBHP}$, $\text{DMP}$, $\text{IBX}$, $\text{NaClO}_2$, $\text{NaIO}_4$** | Zwingend vor dem Einengen mit **$10\,\%\text{ wässriger }\text{Na}_2\text{S}_2\text{O}_3$- oder $\text{Na}_2\text{SO}_3$-Lösung** (bei DMP als **$1:1$-Gemisch mit ges. $\text{NaHCO}_3$**) rühren und mit **KI-Stärke-Papier** auf Peroxidfreiheit prüfen (muss weiß bleiben!). | Einengen von Lösungen, die noch Peroxide oder Ozonide enthalten, führt zu **schweren Explosionen am Rotationsverdampfer**! |
| **$\text{OsO}_4$** | Rühren ($30\text{--}60\text{ min}$) mit ges. wässriger **$\text{Na}_2\text{SO}_3$- oder $\text{Na}_2\text{S}_2\text{O}_5$-Lösung** im Abzug (oder festem $\text{Na}_2\text{SO}_3$ + Celite), bis das schwarze $\text{Os(IV)}$-Oxid ausgefallen ist. | Verhindert das Austreten hochtoxischer, augenschädigender $\text{OsO}_4$-Dämpfe beim Einengen. |
| **$\text{Cr(VI)}$ (Jones, PCC, PDC)** | **Jones:** Tropfenweise **$i\text{-PrOH}$** bei $0\,^\circ\text{C}$ bis rein grün ($\text{Cr}^{3+}$). **PCC:** Verdünnen mit $\text{Et}_2\text{O}$ + Celite und Filtration über **Florisil/Silica-Pad**. | Niemals Chrom-Rückstände ins normale Abwasser gießen ($\text{Cr(VI)}$ ist kanzerogen!). |
| **$(\text{COCl})_2, \text{SOCl}_2, \text{POCl}_3, \text{Tf}_2\text{O}$** | Bei $0\,^\circ\text{C}$ sehr langsam auf **Eiswasser** oder **ges. $\text{NaHCO}_3$-Lösung** gießen ($\text{CO}_2\uparrow$, $\text{HCl}\uparrow$, $\text{SO}_2\uparrow$ – heftige Gasentwicklung!). | Bei Swern entsteht zusätzlich $\text{Me}_2\text{S}$ und $\text{CO}\uparrow$ $\rightarrow$ Abluft durch $\text{NaOCl}$-Wäscher! |
| **$\text{SnBu}_3\text{-X}$ (Stille / $\text{Bu}_3\text{SnH}$)** | Kräftig rühren mit **$10\,\%\text{ wässriger }\text{KF}$-Lösung** ($1\text{--}2\text{ h}$), ausgefallenes polymeres $\text{Bu}_3\text{SnF}\downarrow$ über Celite abfiltrieren (oder Säule mit $10\,\%\,\text{KF}$/$90\,\%$ Silica). | Entfernt hochtoxische, unpolare Zinn-Beiprodukte fast quantitativ vor der Endreinigung. |
| **$\text{DMF}$, $\text{DMSO}$, $\text{NMP}$, $\text{Pyridin}$** | Mit $\text{Et}_2\text{O}$, $\text{MTBE}$ oder $\text{EtOAc/Hexan}$ ($1:1$) verdünnen und **$4\text{--}5\times$ mit Wasser**, **Brine** oder **$5\,\%\,\text{LiCl}$-Lösung** (für $\text{DMF}$) waschen; Pyridin mit $1\,\text{M HCl}$ bzw. ges. $\text{CuSO}_4$ auswaschen oder $3\times$ mit **Toluol co-evaporieren**. | Reines $\text{EtOAc}$ extrahiert viel $\text{DMF}$/$\text{DMSO}$ zurück in die organische Phase $\rightarrow$ $\text{Et}_2\text{O}$ oder $\text{EtOAc/Hexan}$ ($1:1$) verwenden! |

---

<a id="sec-7"></a>
### 2.2 Flüssig-Flüssig-Extraktion: Verteilungsgesetz, Phasenbestimmung & Säure-Base-Trennungs-Kaskade

#### A. Mathematisches Gesetz der Mehrfachextraktion (`Multiple Extractions`)
Der Nernstsche Verteilungskoeffizient $K$ bestimmt die Aufteilung eines Stoffes zwischen organischer Phase und Wasserphase:
$$K = \frac{C_{\text{org}}}{C_{\text{aq}}} = \frac{m_{\text{org}} / V_{\text{org}}}{m_{\text{aq}} / V_{\text{aq}}}$$
Nach $n$ aufeinanderfolgenden Extraktionen jeweils frischen organischen Volumens $V_{\text{org}}$ aus einem wässrigen Volumen $V_{\text{aq}}$ verbleibt in der Wasserphase der Restanteil $q^n$:
$$\text{Restanteil in } \text{H}_2\text{O} = \left(\frac{V_{\text{aq}}}{V_{\text{aq}} + K \cdot V_{\text{org}}}\right)^n$$
> **Goldenes Praxis-Gesetz:** **3-maliges Extrahieren mit je $1/3$ des Volumens ($3 \times 33\text{ mL}$)** entfernt dramatisch mehr Produkt aus der Wasserphase als **1-maliges Extrahieren mit dem gesamten Volumen ($1 \times 100\text{ mL}$)**!
> *Rechenbeispiel ($K = 2.0$, $V_{\text{aq}} = 100\text{ mL}$, Gesamt-$V_{\text{org}} = 100\text{ mL}$):*
> - **1× $100\text{ mL}$:** Rest in $\text{H}_2\text{O} = \frac{100}{100 + 2 \cdot 100} = 33.3\,\% \implies$ Ausbeute $= \mathbf{66.7\,\%}$.
> - **3× $33.3\text{ mL}$:** Rest in $\text{H}_2\text{O} = \left(\frac{100}{100 + 2 \cdot 33.3}\right)^3 = (0.600)^3 = 21.6\,\% \implies$ Ausbeute $= \mathbf{78.4\,\%}$!

#### B. Sichere Bestimmung der Phasen (`Which Layer is Which?`, LibreTexts 4.04)
1. **Dichtevergleich:** Organische Lösungsmittel mit $\rho < 1.0\text{ g/mL}$ (Hexan $0.66$, $\text{Et}_2\text{O } 0.71$, $\text{MTBE } 0.74$, Toluol $0.87$, $\text{EtOAc } 0.90$) schwimmen **oben**; halogenierte Lösungsmittel ($\text{DCM } 1.33$, $\text{DCE } 1.25$, $\text{CHCl}_3\text{ } 1.49$) liegen **unten**. *(Ausnahme: Sehr konzentrierte Salzlösungen [z. B. ges. $\text{K}_2\text{CO}_3$, $\text{Cs}_2\text{CO}_3$, $\text{ZnCl}_2$] oder $6\,\text{M H}_2\text{SO}_4$ können dichter sein als $\text{DCM}$ und die Reihenfolge umkehren!)*
2. **Der Wassertropfen-Test (100 % zuverlässig!):** Lässt man aus einer Pasteur-Pipette $1\text{--}2$ Tropfen reines Wasser in die obere Phase des Scheidetrichters fallen:
   - **Vermischt sich der Tropfen sofort unsichtbar** mit der oberen Schicht $\implies$ die **OBERE Phase ist wässrig**!
   - **Sinkt der Tropfen als perlenförmiges Kügelchen durch die obere Schicht hindurch** bis zur Phasengrenze $\implies$ die **OBERE Phase ist organisch**!
3. **Verbot des Wegwerfens (`Golden Rule`):** **NIEMALS** die wässrige (oder irgendeine) Phase vor dem vollständigen Einengen, Wiegen und NMR-Check der organischen Phase in den Ausguss kippen!

#### C. Vollständiges Säure-Base-Trennungs-Schema (LibreTexts 4.08)

Zur Trennung eines komplexen Gemisches aus **starker organischer Säure** ($\text{R-CO}_2\text{H}$ / $\text{R-SO}_3\text{H}$, $\text{p}K_\text{S} \approx 1\text{--}5$), **schwacher organischer Säure** ($\text{Ar-OH}$ / Phenol, $\text{p}K_\text{S} \approx 9\text{--}10$), **organischer Base** ($\text{R-NH}_2$ / $\text{R}_2\text{NH}$ / Pyridin, $\text{p}K_\text{S}(\text{BH}^+) \approx 4\text{--}11$) und **Neutralstoff** (Ester, Keton, Ether, Aromat):

1. **Lösen:** Gemisch vollständig in einem mit Wasser nicht mischbaren Lösungsmittel ($\text{Et}_2\text{O}$, $\text{MTBE}$, $\text{EtOAc}$ oder $\text{DCM}$) lösen.
2. **Schritt 1 – Extraktion der Base ($\text{R-NH}_2$):**
   - Organische Phase **$3\times$ mit $1\text{--}2\,\text{M wässriger HCl}$** ausschütteln $\rightarrow$ Amine protonieren zu wasserlöslichen Ammoniumchloriden ($\text{R-NH}_3^+\text{Cl}^-$) und wandern in die **wässrige Phase A**.
   - **Rückgewinnung der Base:** Wässrige Phase A im Eisbad kühlen, mit **$2\,\text{M wässriger NaOH}$** (oder $5\,\%\,\text{NaOH}$) vorsichtig auf **$\text{pH } 9\text{--}10$** (pH-Papier!) alkalisieren $\rightarrow$ freies Amin fällt aus oder wird **$3\times$ mit $\text{DCM}/\text{Et}_2\text{O}$** (je $1/3$ des Volumens) rückextrahiert, mit Brine gewaschen, getrocknet ($\text{K}_2\text{CO}_3$ oder $\text{Na}_2\text{SO}_4$) und eingeengt.
3. **Schritt 2 – Selektive Extraktion starker Säuren ($\text{R-CO}_2\text{H}$ neben Phenolen!):**
   - Verbleibende organische Phase **$3\times$ mit $5\,\%\text{ wässriger }\text{NaHCO}_3$-Lösung** ($\text{pH } 8.5$) ausschütteln (**häufig und vorsichtig entlüften!** $\text{CO}_2\uparrow$-Druckentwicklung!).
   - $\text{NaHCO}_3$ ($\text{p}K_\text{S}(\text{H}_2\text{CO}_3) = 6.35$) deprotoniert **ausschließlich Carbonsäuren ($\text{p}K_\text{S} \approx 4\text{--}5$)** quantitativ zu wasserlöslichem $\text{R-CO}_2^-\text{Na}^+$ (**wässrige Phase B**), während **Phenole ($\text{p}K_\text{S} \approx 10$)** unprotoniert in der organischen Phase verbleiben! *(Zudem ist $\text{NaHCO}_3$ so mild, dass im Neutralteil vorhandene Ester nicht verseift werden!)*
   - **Rückgewinnung der Carbonsäure:** Wässrige Phase B im Eisbad kühlen, mit **$2\,\text{M HCl}$** (oder tropfenweise konz. $\text{HCl}$ bei großen Mengen zur Volumenbegrenzung) auf **$\text{pH } 3\text{--}4$** ansäuern (**Vorsicht: starkes Schäumen durch $\text{CO}_2\uparrow$!**). Große Kristalle absaugen; andernfalls (Öl oder feine Kristalle verstopfen Filterpapier!) **$3\times$ mit $\text{EtOAc}/\text{DCM}$** rückextrahieren, Brine-waschen, über $\text{MgSO}_4/\text{Na}_2\text{SO}_4$ trocknen und einengen.
4. **Schritt 3 – Extraktion schwacher Säuren (Phenole $\text{Ar-OH}$):**
   - Verbleibende organische Phase **$3\times$ mit $5\,\%\text{ wässriger NaOH}$** ($\text{pH } 13\text{--}14$) ausschütteln $\rightarrow$ Phenole deprotonieren zu wasserlöslichem $\text{Ar-O}^-\text{Na}^+$ (**wässrige Phase C**).
   - **Rückgewinnung des Phenols:** Wässrige Phase C im Eisbad mit **$2\,\text{M HCl}$ auf $\text{pH } 3\text{--}4$** ansäuern, **$3\times$ mit $\text{Et}_2\text{O}/\text{EtOAc}$** rückextrahieren, Brine-waschen, trocknen und einengen.
5. **Schritt 4 – Isolierung der Neutralstoffe:**
   - Die verbleibende organische Phase enthält nur noch die Neutralkomponenten $\rightarrow$ $1\times$ mit Wasser/Brine waschen, über $\text{MgSO}_4/\text{Na}_2\text{SO}_4$ trocknen und am Rotationsverdampfer einengen.

---

<a id="sec-8"></a>
### 2.3 Praktische Problemlösung im Scheidetrichter: Emulsionen, Brine, Trocknungsmittel & Rotationsverdampfer

#### A. 6 Bewährte Methoden zum Brechen stabiler Emulsionen
1. **Zeit & sanftes Kreisen:** Den offenen Scheidetrichter $10\text{--}15\text{ min}$ ruhig stehen lassen oder langsam mit einem Glasstab an der Grenzfläche kreisen (nicht erneut schütteln!).
2. **Brine-Zugabe (gesättigte $\text{NaCl}$-Lösung):** Erhöht die Ionenstärke und Dichtedifferenz der Wasserphase massiv – bricht über $80\,\%$ aller Öl-in-Wasser-Emulsionen sofort.
3. **Zugabe von mehr organischem Lösungsmittel** (verdünnt grenzflächenaktive Polymere/Seifen und verändert das Dichte- und Viskositätsverhältnis).
4. **Filtration über ein Celite-Pad** (oder Glaswolle/Baumwollpfropf unter leichtem Vakuum): Mechanisches Koaleszieren der Tröpfchen und Zurückhalten von feinen unlöslichen Feststoffen/Aluminiumhydroxid-Partikeln, die Emulsionen stabilisieren (`Pickering-Emulsion`).
5. **Zentrifugation** (für kleinere/mittlere Volumina in verschließbaren Zentrifugenröhrchen die schnellste 100%-Lösung!).
6. **Einige Tropfen Ethanol, Methanol oder Aceton** vorsichtig zugeben (ändert die Oberflächenspannung).

#### B. Vollständige Referenz-Tabelle der Trocknungsmittel (inkl. Kapazitäten aus LibreTexts 4.07 & Prozesschemie)

> **Vorgehensweise beim Trocknen:** 1. Organische Phase immer im **Erlenmeyerkolben** (nicht Becherglas!) trocknen. 2. Eventuelle am Boden oder oben sichtbare Wassertropfen vorher mit einer Pasteur-Pipette absaugen! 3. Bei $\text{EtOAc}$ ($2.92\text{ g H}_2\text{O/100 mL}$) und $\text{Et}_2\text{O}$ ($1.24\text{ g H}_2\text{O/100 mL}$) zwingend **vorher einmal mit Brine waschen**, um möglichst wenig Trocknungsmittel zu verbrauchen (große Mengen Trocknungsmittel adsorbieren Produkt auf ihrer Oberfläche und senken die Ausbeute!). 4. Portionsweise (erbsengroß) zugeben und schwenken, bis kein Verklumpen mehr auftritt, die Lösung glasklar wird und beim Schwenken feine, frei schwebende Partikel („Schneegestöber“) sichtbar bleiben. 5. Abfiltrieren (bei $\text{MgSO}_4$) oder Abdekantieren (bei $\text{Na}_2\text{SO}_4$) und Filterkuchen **mit frischem trockenem Lösungsmittel nachspülen**!

| Trocknungsmittel | Gebildete Hydrate | Wasser-Kapazität ($\text{g H}_2\text{O} / \text{g Trockenmittel}$) | Trocknungs-geschwindigkeit | Restwasser-Effizienz | Kompatibilität, Inkompatibilitäten & Labor-Hinweise |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Magnesiumsulfat ($\text{MgSO}_4$)** | $\text{MgSO}_4\cdot 7\text{H}_2\text{O}$ | **$0.15\text{--}0.75\text{ g/g}$** | **Sehr schnell** | **Hoch** | **Universal-Standard (`Go-To`)**; trocknet selbst $\text{Et}_2\text{O}$ und $\text{EtOAc}$ schnell. Feines Pulver $\rightarrow$ muss abfiltriert und **nachgewaschen** werden (adsorbiert polare Produkte!). **Inkompatibilität:** $[\text{Mg(H}_2\text{O)}_4]^{2+}$ ist schwach **Lewis-sauer** $\rightarrow$ für extrem säureempfindliche Gruppen (`TMS`, `THP`, Vinyl-Epoxide, empfindliche Acetale) besser $\text{Na}_2\text{SO}_4$ oder $\text{K}_2\text{CO}_3$ verwenden! |
| **Natriumsulfat ($\text{Na}_2\text{SO}_4$)** | $\text{Na}_2\text{SO}_4\cdot 7\text{H}_2\text{O}$, $\text{Na}_2\text{SO}_4\cdot 10\text{H}_2\text{O}$ | **$1.25\text{ g/g}$** *(höchste Kapazität!)* | Moderat ($10\text{--}30\text{ min}$ stehen lassen!) | Mittel | **Absolut neutral und mild** (sicher für säurelabile Gruppen!). Körnige Kristalle $\rightarrow$ einfaches Abdekantieren ohne großen Produktverlust. **Nachteil:** Trocknet feuchtes $\text{Et}_2\text{O}$ oder $\text{EtOAc}$ ohne vorherige Brine-Wäsche nur unvollständig; oberhalb von $32.4\,^\circ\text{C}$ zerfällt $\text{Na}_2\text{SO}_4\cdot 10\text{H}_2\text{O}$ wieder! |
| **Calciumchlorid ($\text{CaCl}_2$)** | $\text{CaCl}_2\cdot 2\text{H}_2\text{O}$, $\text{CaCl}_2\cdot 6\text{H}_2\text{O}$ | **$0.30\text{ g/g}$** | Schnell | Hoch | Günstiges Granulat für **Trockenrohre** und **Exsikkatoren** sowie unpolare Lösungsmittel (Kohlenwasserstoffe, Halogenalkane). **STRIKTE INKOMPATIBILITÄT:** Bildet unlösliche Koordinationskomplexe mit **Alkoholen ($\text{MeOH, EtOH}$!), Aminen, Amiden, Phenolen, Ketonen und Estern** (niemals für diese Stoffklassen in Lösung nutzen!). |
| **Calciumsulfat ($\text{CaSO}_4$, `Drierite`)** | $\text{CaSO}_4\cdot \frac{1}{2}\text{H}_2\text{O}$, $\text{CaSO}_4\cdot 2\text{H}_2\text{O}$ | Gering ($<0.07\text{ g/g}$) | Sehr schnell | **Extrem hoch** | Mit Cobalt(II)-Indikator: **Blau = trocken**, **Rosa = erschöpft**. Wegen der geringen Kapazität fast nur für **Exsikkatoren, Gastrocknung und Trockenrohre** geeignet, kaum für Workup-Lösungen. |
| **Kaliumcarbonat ($\text{K}_2\text{CO}_3$)** | $\text{K}_2\text{CO}_3\cdot 1.5\text{H}_2\text{O}$, $\text{K}_2\text{CO}_3\cdot 2\text{H}_2\text{O}$ | Mittel | Schnell | Hoch | **Basisch!** Ideal zum Trocknen von **Aminen, Alkaloiden, Hydrazinen, Ketonen und säurelabilen Acetalen**. **Verboten** für Carbonsäuren, Phenole und leicht verseifbare Ester! |
| **$\text{KOH}$ / $\text{NaOH}$ (Plätzchen)** | Hydrate | Hoch | Schnell | Sehr hoch | Ausschließlich zum Vortrocknen von basischen **Aminen, Pyridin, Anilin** (stark basisch und ätzend!). |
| **Molekularsieb (`3Å, 4Å, 5Å`)** | Zeolith-Poren (physikalische Physisorption!) | $\sim 0.20\text{ g/g}$ | Langsam ($12\text{--}24\text{ h}$) | **Höchste ($<5\text{ ppm H}_2\text{O}$!)** | **Goldstandard zur Herstellung wasserfreier Lösungsmittel!** Zwingend vorab im Ofen ($200\text{--}300\,^\circ\text{C}$) oder unter Vakuum mit Brenner/Mikrowelle aktivieren!<br>• **3Å (Pore $0.3\text{ nm}$):** Für **$\text{MeOH}, \text{EtOH}, \text{MeCN}, \text{Aceton}, \text{THF}, \text{DCM}$** (nur $\text{H}_2\text{O}$-Moleküle passen hinein, verhindert Katalyse von Aldol/Ketal-Nebenreaktionen!).<br>• **4Å (Pore $0.4\text{ nm}$):** Für **Toluol, $\text{THF}, \text{Et}_2\text{O}, \text{DMF}, \text{DMSO}, \text{DCM}$** (**NICHT** für $\text{MeOH}$ oder $\text{MeCN}$!). |

#### C. Regeln für den Rotationsverdampfer (`Rotovap`, LibreTexts 5.06)
- **Kolbengröße:** Rundkolben **maximal zu $50\,\%$ füllen**!
- **Auffangkühlfalle & Kondensator:** Vor dem Start entleeren (niemals volle Lösungsmittel-Vorlagen vom Vorgänger übernehmen – Kontaminations- und Mischgefahr!).
- **Sicherheits-Reihenfolge (`Start & Stop`):**
  1. Kolben mit **Keck-Clip** (bzw. bei Vakuum nach Ansaugen zusätzlich halten!) und optional einem **Bump Trap (Spritzschutz-Kugel)** anbringen!
  2. **Rotation einschalten** ($\sim 100\text{--}150\text{ rpm}$), **Vakuum langsam schließen**, warten bis der Kolben fest sitzt und keine Stoßsiedung (`Bumping`) auftritt; erst dann langsam ins Wasserbad ($30\text{--}45\,^\circ\text{C}$, für sehr niedrigsiedende Produkte wie $\text{Et}_2\text{O}$/Pentan **Raumtemperatur ohne Heizen**!) absenken.
  3. **Beenden:** Kolben zuerst **aus dem Wasserbad heben**, **Belüftungshahn langsam öffnen** (wobei man den Kolben festhält!), **danach** Rotation und Vakuumpumpe abschalten!
- **Spuren von Lösungsmittel im Produkt entfernen:** Nach dem Rotovap am **Ölpumpen-Hochvakuum (`Schlenk-Linie`, $<0.5\text{ mbar}$)** abziehen; schwerflüchtige Spuren von $\text{EtOAc}$, $\text{DCM}$ oder $\text{H}_2\text{O}$ durch $2\text{--}3\times$ Aufnehmen in wenig reinem $\text{DCM}$ oder $\text{Et}_2\text{O}$ (bzw. Toluol für Wasser/$\text{AcOH}$) und erneutes Einengen verdrängen.

---

<a id="sec-9"></a>
## 3. Reinigungsverfahren: Umkristallisation, Destillation, Sublimation & Chromatographie

<a id="sec-10"></a>
### 3.1 Umkristallisation (`Crystallization`, LibreTexts Kapitel 3)

1. **Prinzip & Auswahl des Lösungsmittels:**
   - Ein ideales Lösungsmittel löst das gewünschte Produkt bei **Siedehitze sehr gut**, bei **Raumtemperatur oder $0\,^\circ\text{C}$ kaum** (steile Löslichkeitskurve), löst aber Verunreinigungen entweder **immer hervorragend** (bleiben in der Mutterlauge) oder **gar nicht** (Heißfiltration!).
   - **Test-Protokoll im Reagenzglas ($100\text{ mg}$ Feststoff + $3\text{ mL}$ Lösungsmittel):** Wenn sich der Feststoff bereits bei RT komplett löst $\rightarrow$ ungeeignet (zu hohe Löslichkeit); wenn er sich selbst beim Sieden nicht löst $\rightarrow$ ungeeignet (zu geringe Löslichkeit).
   - **Standard-Lösungsmittelpaare (`Mixed Solvents`, Tabelle 3.2 aus LibreTexts 3.3F):**
     In Minimum-Menge heißem **gutem Lösungsmittel** lösen $\rightarrow$ heißes **schlechtes Lösungsmittel (`Antisolvent`)** tropfenweise bis zur beginnenden bleibenden Trübung zugeben $\rightarrow$ mit $1\text{--}3$ Tropfen heißem gutem Lösungsmittel wieder klären $\rightarrow$ langsam abkühlen!
     - **Polare Paare:** Methanol/Wasser, Ethanol/Wasser, Aceton/Wasser
     - **Mittelpolare / Unpolare Paare:** Methanol/Diethylether, **Hexan (Petrolether)/Ethylacetat** (Standard!), Hexan/Diethylether, Dichlormethan/Hexan.
2. **Aktivkohle-Entfärbung & Heißfiltration (`Hot Gravity Filtration`):**
   - Bei stark gefärbten, teerigen Verunreinigungen: Lösung etwas abkühlen lassen (**niemals Aktivkohle in eine siedende Lösung werfen $\rightarrow$ heftiges Überschäumen!**), eine **Spatelspitze Aktivkohle (`Norit/Darco`)** zugeben, $5\text{ min}$ aufkochen und **sofort heiß durch ein vorgewärmtes Faltenfilter (`Fluted Filter Paper`) oder eine beheizte Celite-Schicht** mit wenig heißem Lösungsmittel filtrieren (**kein Vakuum beim Heißfiltrieren**, da das Vakuum das Lösungsmittel sofort verdampft und das Produkt im Trichter/Filter auskristallisiert!).
3. **Kristallisation auslösen, Ernten & Second Crop:**
   - Langsam zunächst an der Luft (auf einem Korkring, nicht direkt auf kalter Laborbank!) auf RT abkühlen lassen (**langsames Abkühlen bildet reine, große Kristalle ohne Einschluss von Verunreinigungen!**), erst danach für $15\text{--}30\text{ min}$ ins **Eisbad** stellen.
   - Bleibt Kristallisation aus: **Glasstab an der inneren Glaswand unter der Flüssigkeitsoberfläche reiben (`Scratching`)** oder einen winzigen **Impfkristall (`Seed Crystal`)** zugeben.
   - **Absaugen (`Suction Filtration`, Büchner- oder Hirsch-Trichter):** Filterpapier mit demselben Lösungsmittel anfeuchten, Kristalle absaugen und **bei abgeschaltetem/getrenntem Vakuum** mit **eiskaltem** schlechtem Lösungsmittel nachwaschen.
   - **Problem „Ausölen“ (`Oiling Out`):** Entsteht, wenn der Feststoff unterhalb der Lösungsmittel-Siedetemperatur schmilzt ($T_{\text{bp, LM}} > T_{\text{mp, Produkt}}$) $\rightarrow$ etwas mehr Lösungsmittel zugeben, sodass der Feststoff bei einer Temperatur unterhalb seines Schmelzpunkts gelöst bleibt, oder auf ein tiefer siedendes Lösungsmittel wechseln!

---

<a id="sec-11"></a>
### 3.2 Destillation & Sublimation (LibreTexts Kapitel 5 & 6.03)

#### A. Auswahl der richtigen Destillationsmethode
| Methode | Einsatzkriterium ($\Delta \text{bp}$ & Siedepunkt) | Kritische Apparatur- & Durchführungspraxis |
| :--- | :--- | :--- |
| **Einfache Destillation** | Verunreinigung ist **nichtflüchtig** ($<10\,\%$) ODER **$\Delta\text{bp} > 100\,^\circ\text{C}$**. | Thermometer-Kugelspitze muss exakt **unterhalb des Seitenarms des Destillieraufsatzes** sitzen (so wird die Dampftemperatur im Gleichgewicht mit dem Kondensat gemessen!). Destillationskolben niemals komplett trocken destillieren (**Explosionsgefahr bei Peroxiden!**). |
| **Fraktionierte Destillation** | Trennung zweier flüchtiger Flüssigkeiten mit **$\Delta\text{bp} < 100\,^\circ\text{C}$** (z. B. $20\text{--}80\,^\circ\text{C}$ Differenz). | Einsatz einer **Vigreux-Kolonne** ($\sim 2\text{--}3$ theoretische Böden), **Füllkörperkolonne** (Glaskugeln/Raschig-Ringe/Stahlwolle: Vorsicht, Stahlwolle reagiert mit $\text{HCl}/\text{Halogeniden}$!) oder Drehbandkolonne. Langsame Destillationsrate ($1\text{ Tropfen/Sekunde}$), um optimales Rücklaufverhältnis für viele Gleichgewichtsstufen (`Raoult-Diagramm`) zu garantieren! **Achtung Azeotrope:** Ethanol/Wasser ($95.6\,\%\text{ EtOH}$, $\text{bp } 78.15\,^\circ\text{C}$) lässt sich durch einfache oder fraktionierte Destillation **nicht** weiter entwässern! |
| **Vakuumdestillation** | Hochsiedende oder thermisch empfindliche Substanzen (**$\text{bp}_{760} > 150\,^\circ\text{C}$**; Verhindert thermische Zersetzung). | • **Claisen-Aufsatz** + kräftiges Magnetrühren (oder feine Gaseinlasskapillare; **KEINE Siedesteine!**).<br>• **Kühlfalle (`Liquid N2 / Dry Ice Trap`)** zwingend zwischen Apparatur und Ölpumpe schalten!<br>• **Ausschalt-Reihenfolge (KRITISCH!):** **1.** Heizbad absenken und Apparatur abkühlen lassen $\rightarrow$ **2.** Langsam über Schutzgas-Hahn (**Argon/$\text{N}_2$**) belüften (damit keine heiße Substanz mit Luft-$\text{O}_2$ verharzt/explodiert!) $\rightarrow$ **3.** Erst dann Vakuumpumpe abschalten (**nie Pumpe ausschalten, solange Vakuum anliegt**, sonst zieht der Kolben Pumpenöl zurück!). |
| **Wasserdampfdestillation** | Wasserunlösliche, hochsiedende Naturstoffe / Öle (**Terpene**, Nelkenöl/Eugenol, Zimtaldehyd), die sich bei $>100\,^\circ\text{C}$ zersetzen würden. | Bei unmischbaren Flüssigkeiten addieren sich die Partialdampfdrücke ($p_{\text{ges}} = p_{\text{H}_2\text{O}}^\circ + p_{\text{Org}}^\circ = 760\text{ Torr}$). Daher co-destilliert das Gemisch **stets unterhalb von $100\,^\circ\text{C}$** (meist $98\text{--}99.5\,^\circ\text{C}$), unabhängig davon, dass der Reinstoff erst bei $250\,^\circ\text{C}$ siedet! |
| **Vakuumsublimation** | Reinsubstanzen mit hohem Dampfdruck im Festzustand (Campher, Ferrocen, Chinone, Koffein, Naphthalin). | **Kühlfinger (`Cold Finger`)** mit Eiswasser oder Trockeneis/Aceton befüllen; Druck langsam auf $<0.5\text{ mbar}$ senken, mild heizen. Vor dem Abkratzen der Kristalle vom Kühlfinger warten, bis er auf RT erwärmt ist (sonst kondensiert sofort Luftfeuchtigkeit auf den reinen Kristallen!). |

#### B. Siedepunkts-Abschätzung bei reduziertem Druck (Tabelle 5.9 aus LibreTexts 5.4B / *Chemist's Companion*)
> **Daumenregel:** Jede **Halbierung des Drucks** senkt den Siedepunkt um ca. **$15\text{--}20\,^\circ\text{C}$**; von $760\text{ Torr}$ auf **$20\text{ Torr}$ (Wasserstrahlvakuum)** sinkt der Siedepunkt um etwa **$90\text{--}120\,^\circ\text{C}$**; auf **$0.1\text{ Torr}$ (Ölpumpe)** um etwa **$160\text{--}190\,^\circ\text{C}$**!

| Normaldruck $\text{bp}_{760\text{ mmHg}}$ ($^\circ\text{C}$) | $\mathbf{150}$ | $\mathbf{170}$ | $\mathbf{200}$ | $\mathbf{220}$ | $\mathbf{250}$ | $\mathbf{270}$ | $\mathbf{300}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$\text{bp}$ bei $20\text{ mmHg}$ ($\sim 27\text{ mbar}$)** | $62$ | $78$ | $101$ | $117$ | $141$ | $157$ | $181$ |
| **$\text{bp}$ bei $18\text{ mmHg}$ ($\sim 24\text{ mbar}$)** | $60$ | $76$ | $99$ | $115$ | $139$ | $154$ | $178$ |
| **$\text{bp}$ bei $16\text{ mmHg}$ ($\sim 21\text{ mbar}$)** | $58$ | $73$ | $97$ | $112$ | $136$ | $151$ | $174$ |
| **$\text{bp}$ bei $14\text{ mmHg}$ ($\sim 19\text{ mbar}$)** | $56$ | $71$ | $94$ | $108$ | $133$ | $148$ | $171$ |
| **$\text{bp}$ bei $12\text{ mmHg}$ ($\sim 16\text{ mbar}$)** | $52$ | $68$ | $90$ | $104$ | $129$ | $144$ | $167$ |

---

<a id="sec-12"></a>
### 3.3 Dünnschichtchromatographie (`DC`/`TLC`), Anfärbereagenzien & Säulenchromatographie

#### A. DC-Optimierung, Co-Spot-Gesetz & Elutionskraft (Eluotrope Reihe)
1. **Retention Factor ($R_f$):** $R_f = \frac{\text{Laufstrecke Substanzzentrum}}{\text{Laufstrecke Laufmittelfront}}$ (stets $0.00 \le R_f \le 1.00$).
   - **Optimaler $R_f$ für die Säulenchromatographie:** Laufmittelgemisch so optimieren, dass das gewünschte Produkt einen **$R_f$-Wert zwischen $0.20$ und $0.35$** besitzt (bei sehr ähnlichen Komponenten: $\Delta R_f \ge 0.15$ anstreben; falls zu eng, auf $\text{Et}_2\text{O}/\text{Hexan}$, $\text{DCM}/\text{Hexan}$ oder Toluol/EtOAc wechseln!).
2. **Das Co-Spot-Gesetz (`Co-Spotting`):** Um Reaktionsfortschritt sicher zu beurteilen, trägt man auf **einer** DC-Platte immer mindestens 3 Bahnen auf: **1. Edukt (`SM`)**, **2. Co-Spot (`SM + Reaktion` übereinander!)**, **3. Reaktionsmischung (`RM`)**. Nur wenn der Co-Spot sauber aufspaltet (oder Edukt verschwindet), weiß man sicher, ob Produkt und Edukt wirklich unterschiedliche $R_f$-Werte haben oder zufällig co-eluieren!
3. **Streifenbildung (`Streaking / Tailing`) verhindern:**
   - **Carbonsäuren ($\text{RCO}_2\text{H}$)** ziehen auf Kieselgel wegen Deprotonierung/H-Brücken lange Schweife $\rightarrow$ **$0.5\text{--}1\,\%\text{ Essigsäure (AcOH)}$ oder Ameisensäure** zum Laufmittel geben!
   - **Amine ($\text{RNH}_2, \text{R}_2\text{NH}, \text{Pyridine}$)** kleben an den sauren Silanol-Gruppen ($\text{Si-OH}$) des Kieselgels auf der Startlinie ($R_f = 0$) $\rightarrow$ **$1\text{--}2\,\%\text{ Triethylamin ($\text{Et}_3\text{N}$)}$ oder $\text{NH}_4\text{OH}/\text{MeOH}$** zum Laufmittel geben (oder **basisches Aluminiumoxid** verwenden!).
4. **Eluotrope Reihe für Kieselgel (`Silica Gel 60`) – zunehmende Elutionskraft (Polarität):**
   $$\text{Hexan / Pentan} < \text{Cyclohexan} < \text{Toluol} < \text{Et}_2\text{O} \approx \text{MTBE} < \text{DCM} < \text{CHCl}_3 < \text{EtOAc} < \text{Aceton} < \text{MeCN} < i\text{-PrOH} < \text{EtOH} < \text{MeOH}$$
   *(**Praxis-Regel für binäre Laufmittel:** Standard-Screening = **Hexan/EtOAc** [9:1 $\rightarrow$ 1:1], für sehr polare Amine/Zucker/Säuren = **DCM/MeOH** [98:2 $\rightarrow$ 85:15]; **NIEMALS $>15\,\%\text{ MeOH}$ in DCM** auf Kieselgel verwenden, da Methanol das Kieselgel selbst merklich löst und mit durch die Säule spült!).*

#### B. Vollständige Tabelle der DC-Visualisierungs- & Anfärbereagenzien (Rezepturen aus LibreTexts 2.3F & Synthesepraxis)

| Visualisierung / Tauchreagenz | Exakte Labor-Rezeptur & Lagerung | Mechanismus & Angefärbte Stoffklassen (Selektivität) | Resultierende Spot-Farbe & Kritische Anwendungshinweise |
| :--- | :--- | :--- | :--- |
| **UV-Lampe ($\lambda = 254\text{ nm}$)** | Zerstörungsfrei! Auf Kieselgel-Platten mit Fluoreszenzindikator ($\text{F}_{254}$, Zinksilikat). | Konjugierte $\pi$-Systeme (Aromaten, Enone, konjugierte Diene, Sulfonamide, Azide) absorbieren $254\text{ nm}$ UV-Licht und löschen die grüne Hintergrund-Fluoreszenz (`Quenching`). | **Dunkelviolette/schwarze Flecken** auf hellgrünem Grund. **Immer zuerst vor dem Tauchen durchführen** und Spots mit weichem Bleistift umranden! Gesättigte Alkohole, Alkene, Ketone und Ester sind **UV-inaktiv**! |
| **Iod-Kammer ($\text{I}_2$ auf Kieselgel)** | Schraubglas mit einigen $\text{I}_2$-Kristallen + trockenem Kieselgel füllen; Platte $1\text{--}5\text{ min}$ hineinstellen. | Reversibel! Iod bildet braune Charge-Transfer-Komplexe mit Doppelbindungen ($\text{C=C}$), Aromaten, Aminen, Ethern und manchen Carbonylen. | **Gelbbraune Spots** (verblassen an der Luft wieder, daher sofort mit Bleistift markieren!). Aromatische Ketone wie Acetophenon färben mit $\text{I}_2$ manchmal kaum. |
| **Kaliumpermanganat ($\text{KMnO}_4$)** | **$1.5\text{ g KMnO}_4$ + $10\text{ g K}_2\text{CO}_3$ + $1.25\text{ mL } 10\,\%\text{ NaOH}$ in $200\text{ mL H}_2\text{O}$** (stabil für Monate). | **Universelles Oxidations-Reagenz:** Reduktion von violettem $\text{MnO}_4^-$ zu braun/gelbem $\text{MnO}_2$ durch **Alkene, Alkine, $1^\circ/2^\circ$-Alkohole, Aldehyde, Amine, Thiole, Phenole, Zucker**. *(Alkane, Benzol, Ketone, Ester, Carbonsäuren reagieren kaum!)* | **Leuchtend gelbe Spots** auf tiefviolettem/rosa Grund (meist reicht kurzes Erwärmen oder sofort bei sehr reaktiven Alkenen/Aldehyden!). |
| ***para*-Anisaldehyd-Tauchreagenz** | **$135\text{ mL EtOH abs.}$ + $5\text{ mL konz. H}_2\text{SO}_4$ + $1.5\text{ mL Eisessig (AcOH)}$ + $3.7\text{ mL } p\text{-Anisaldehyd}$** (in Alufolie im **Kühlschrank** lagern; Haltbarkeit $\sim 6\text{ Monate}$). | Säurekatalysierte Acetalisierung / elektrophile Kondensation mit starken und schwachen Nucleophilen (**Alkohole, Phenole, Zucker, Terpene, Enolether, Acetale, Aldehyde, Ketone, viele Amine**). *(Unreaktiv: reine Alkene, unsubst. Aromaten, Ester, Carbonsäuren!)* | **Kräftige Regenbogen-Farben** (Blau, Violett, Grün, Türkis, Pink, Braun auf zartrosa Grund – ermöglicht oft die Unterscheidung verschiedener Isomere allein über den Farbton!). **Stark ätzend/sauer!** |
| **Vanillin-Tauchreagenz** | **$250\text{ mL EtOH}$ + $15\text{ g Vanillin}$ + $2.5\text{ mL konz. H}_2\text{SO}_4$** (in Alufolie im Kühlschrank; verwerfen, sobald sich die Lösung blau verfärbt!). | Säurekatalysierte Kondensation ähnlich *p*-Anisaldehyd (**Alkohole, Phenole, Ketone, Aldehyde, Terpene, Steroide**). *(Unterschied zu $p$-Anisaldehyd: Zimtsäure färbt stark mit Vanillin, Zimtaldehyd mit $p$-Anisaldehyd!)* | **Blau, Violett, Rosa, Gelb, Schwarz** nach mildem Erhitzen mit der Heißluftpistole (`Heat Gun`). |
| **Phosphormolybdänsäure (`PMA`)** | **$5\text{ g Phosphormolybdänsäure}$ in $500\text{ mL EtOH}$** (oder $10\,\%$ in $\text{EtOH}$, lichtempfindlich $\rightarrow$ Alufolie!). | **Universelles Redox-Reagenz:** Reduktion von $\text{Mo(VI)}$ zu gemischtem Molybdänblau durch fast **alle organischen Stoffe** (Alkohole, Alkene, Alkylether, Alkyliodide, Steroide, Lipide, Carbonyle, viele Aromaten). | **Dunkelblaue bis schwarzblaue Spots** auf gelbgrünem Grund nach kräftigem Erhitzen! *(Alternative für extrem empfindliche Lipid-/Zucker-Nachweise: **Cer(IV)-Ammoniummolybdat `CAM` / Hanessian-Stain**: $2.5\text{ g }\text{Ce(SO}_4)_2 + 6.25\text{ g }(\text{NH}_4)_6\text{Mo}_7\text{O}_{24} + 25\text{ mL }\text{H}_2\text{SO}_4\text{ in } 225\text{ mL H}_2\text{O} \rightarrow$ extrem empfindliche tiefblaue Spots!).* |
| **Ninhydrin-Reagenz** | $0.3\text{ g Ninhydrin}$ in $100\text{ mL } n\text{-BuOH}$ + $3\text{ mL AcOH}$ (oder $1.5\text{ g Ninhydrin}$ in $100\text{ mL } n\text{-BuOH}$ + $3\text{ mL AcOH}$). | **Spezifisch für primäre und sekundäre Amine, Aminosäuren, Peptide** (und `Boc`-geschützte Amine nach starkem Erhitzen, da die Säure/Hitze `Boc` spaltet!). | **Tiefviolett (`Ruhemanns Purpur`)** für $1^\circ$-Amine; **Gelb/Orange** für $2^\circ$-Amine wie Prolin! |
| **Bromkresolgrün (`Bromocresol Green`)** | $0.04\text{ g Bromkresolgrün}$ in $100\text{ mL EtOH}$, tropfenweise $0.1\,\text{M NaOH}$ zugeben, bis Lösung gerade **blaugrün** wird. | **Spezifisch für Carbonsäuren ($\text{p}K_\text{S} < 5$)** (pH-Indikatorumschlag: blau bei $\text{pH}>5.4$, gelb bei $\text{pH}<3.8$). | **Gelbe Spots auf blauem Hintergrund** (sofort ohne Erhitzen sichtbar!). **Phenole** ($\text{p}K_\text{S} \approx 10$) färben **nicht** gelb! |
| **2,4-Dinitrophenylhydrazin (`2,4-DNPH`)** | $3\text{ g 2,4-DNPH}$ in $15\text{ mL konz. H}_2\text{SO}_4 + 20\text{ mL H}_2\text{O} + 70\text{ mL EtOH}$. | **Spezifisch für Aldehyde und Ketone** (Hydrazon-Bildung). | **Gelb-Orange** (nicht-konjugierte Carbonyle) bis **Tiefrot** (konjugierte Enale/Arylketone), sofort ohne Erhitzen sichtbar. |
| **Eisen(III)-chlorid ($\text{FeCl}_3$)** | $1\text{--}5\,\%\text{ FeCl}_3$ in $\text{H}_2\text{O}$ oder $\text{EtOH}$ (mit $1\,\%\text{ HCl}$). | **Spezifisch für Phenole und Enole** (1,3-Diketone). | **Tiefblau, Violett, Rot oder Grün** ohne Erhitzen. |

#### C. Flash- & Säulenchromatographie (Still-Kriterien, LibreTexts 2.04)
1. **Kieselgel-Menge (`Silica-to-Sample Ratio`):**
   - Einfache Trennung ($\Delta R_f > 0.25$): **$20\text{--}30\text{ g}$ Kieselgel pro $1\text{ g}$ Rohprodukt**.
   - Standard-Trennung ($\Delta R_f = 0.10\text{--}0.20$): **$40\text{--}60\text{ g}$ Kieselgel pro $1\text{ g}$ Rohprodukt**.
   - Schwierige Trennung ($\Delta R_f < 0.10$): **$80\text{--}100\text{ g}$ Kieselgel pro $1\text{ g}$ Rohprodukt** (bzw. Säulenlänge $15\text{ cm}$ Schüttung, Durchmesser nach Tabellennorm).
2. **Packen & Auftragen (`Slurry Packing` & `Liquid vs. Dry Loading`):**
   - **Sicherheit:** Trockenes Kieselgel (`Silica 60, 40–63 μm`) und Aluminiumoxid sind **alveolengängige Lungenreizstoffe (Silikose-Gefahr!)** $\rightarrow$ **ausschließlich im Abzug** abwiegen und anschlämmen!
   - **Exotherme Solvatation:** Beim Anrühren der Kieselgel-Slurry mit Laufmittel entsteht Wärme $\rightarrow$ Slurry rühren, entgasen und vor dem Einfüllen abkühlen lassen, damit sich keine Luftblasen/Risse in der Säule bilden. **Die weiße Adsorbens-Säule darf während der gesamten Trennung niemals trockenlaufen!**
   - **Probenauftrag (`Loading`):** Ideal als **konzentrierte Lösung in möglichst unpolarem Laufmittel** (z. B. reines $\text{DCM}$ oder Laufmittelgemisch; **niemals** in polarem $\text{MeOH}$, $\text{DMSO}$ oder reinem $\text{EtOAc}$ für eine unpolare Hexan-Säule, da sonst die gesamte Bande vorzeitig verschmiert!). Ist das Rohprodukt unlöslich $\rightarrow$ **Dry Loading auf Celite oder Kieselgel** (Produkt in $\text{DCM/MeOH}$ lösen, mit $2\text{--}3\text{ Gewichtsteilen}$ grobem Kieselgel/Celite versetzen, am Rotovap zur rieselfähigen Trockne einengen und als schmale Schicht auf den Sand aufgeben!).
3. **Säule leeren nach Abschluss:** Druckluft/Stickstoff durch die Säule pressen, bis das Kieselgel komplett trocken ist, und **im Abzug** in den Sondermüll-Feststoffbehälter entleeren.

---

<a id="sec-13"></a>
### 3.4 Gaschromatographie (`GC`), Chirale HPLC/SFC & Prozess-Kristallisation (`Scale-up`)

1. **Gaschromatographie (`GC`, LibreTexts 2.05 & `analytical-chemist`):**
   - **Proben-Vorbereitung:** Nur flüchtige, thermisch stabile, **wasserfreie** (über $\text{MgSO}_4/\text{Na}_2\text{SO}_4$ getrocknete!) Proben in niedrig siedendem Lösungsmittel ($\text{DCM}, \text{Et}_2\text{O}, \text{Hexan}, \text{EtOAc}$; verdünnt $\sim 1\text{ mg/mL}$) injizieren (**kein Wasser** in MS-Detektoren, keine nicht-flüchtigen Salze!).
   - **Inlet-Diskriminierung (Hochsieder-Verlust):** Bei hochsiedenden Analyten (z. B. schwere PAKs) auf **Cold On-Column** oder **PTV-Inlet** wechseln; bei **Headspace-Sättigung** flüchtiger Stoffe stark verdünnen.
   - **Säulenbluten (`Column Bleed`) vs. Ghost Peaks:** Durch Blindgradienten bis zur Endtemperatur bestätigen; Septum/Liner regelmäßig reinigen.
2. **HPLC, Chirale Trennung & Van-Deemter-Skalierung:**
   - **Van-Deemter-Gleichung:** $\text{HETP} = A + \frac{B}{u} + C \cdot u$ (optimale Lineargeschwindigkeit $u$ minimiert die Bodenhöhe $\text{HETP}$).
   - **Kritische Auflösungs- und Asymmetriekriterien:** In der regulierten Analytik gilt **$R_s \ge 1.5\text{--}2.0$** für kritische Peakpaare; Asymmetriefaktor **$A_s \approx 1.0$** ($A_s > 1.2$ = Tailing durch Säulenüberladung, Hohlräume [`Voids`], aktive Silanolstellen oder falschen pH).
   - **RP-Prep-HPLC-Modifier-Falle:** **TFA** ($0.1\,\%$) verbessert zwar die Peakform basischer Amine, **TFA-Salze verbreitern aber nachfolgende $^1\text{H}$-NMR-Signale** massiv und stören Zellassays $\rightarrow$ für NMR/Bioassays **Ameisensäure ($\text{HCO}_2\text{H}$)** oder $\text{NH}_4\text{HCO}_3$ bevorzugen oder nachträglich mit $\text{HCl/NaHCO}_3$ entsalzen!
   - **Chirale HPLC / SFC:** Immer Racemat zur Kalibrierung injizieren, Säule, Eluent, Temperatur, Fluss, Wellenlänge und Integrationsmethode für den $\text{ee}$-Wert exakt dokumentieren; Detektorsättigung am Hauptenantiomer ausschließen!
3. **Prozesschemie-Kristallisation, Polymorphie & Scale-up (`process-chemist`, `green-chemist`, `crystallographer`):**
   - **Metastabile Zonenbreite (`MSZW`):** Betrieb innerhalb der MSZW (zwischen Löslichkeitskurve und spontaner Nukleation) mit definiertem **Impfen (`Seeding`: Seed-Masse, Partikelgrößenverteilung `PSD`, Zugabetemperatur)**; **Warnung:** MSZW aus dem mL-Maßstab ist **nicht linear skalierbar** (im Rührkessel dominiert Sekundärnukleation durch Rührblatt-Kollisionen $\rightarrow$ In-situ-Kontrolle mit **FBRM** / **PVM**).
   - **Massen-Metriken & Green Chemistry:**
     - **Atomökonomie (`AE`):** $\frac{M_{\text{Produkt}}}{\sum M_{\text{Edukte}}} \times 100\,\%$
     - **Reaction Mass Efficiency (`RME`):** $\frac{m_{\text{Produkt}}}{m_{\text{alle Reaktanten}}} \times 100\,\%$
     - **Process Mass Intensity (`PMI`):** $\frac{\sum m_{\text{alle Eingaben (inkl. alle Lösungsmittel, Waschwässer, Katalysatoren, Filterhilfsmittel)}}}{m_{\text{isoliertes Produkt}}}$ *(Waschwässer wegzulassen verfälscht PMI/E-Faktor!)*
     - **Sheldon E-Faktor:** $\frac{m_{\text{Gesamtabfall}}}{m_{\text{Produkt}}} = \text{PMI} - 1$ (Feinchemie typ. $5\text{--}50$; Pharma oft $>100$).
   - **Prozesssicherheit & Kalorimetrie (`RC1`, `ARC`, `MTSR`):** Vor jedem Scale-up exothermer Reaktionen $\Delta H_{\text{rxn}}$, den adiabatischen Temperaturanstieg $\Delta T_{\text{ad}} = \frac{-\Delta H_{\text{rxn}}}{C_p \cdot m}$ und die **Maximum Temperature of Synthetic Reaction (`MTSR`)** gegen Zersetzungstemperaturen (`DSC`/`ARC`) und die reale Anlagen-Kühlkapazität prüfen! **Lösungsmittelwechsel (`DCM` $\rightarrow$ `EtOAc` / `2-MeTHF`)** erfordert stets eine erneute Prüfung von Verteilungskoeffizienten, Polymorphie (`XRPD`/`DSC`) und Kalorimetrie!
   - **ICH Q3C / Q3D:** Restlösungsmittel (Class 1–3) per GC-Headspace und Schwermetall-Spuren ($\text{Pd}, \text{Ni}, \text{Ru}$) per **ICP-MS** prüfen (Abreicherung über Scavenger wie **SMMP** oder **Darco**/Aktivkohle).

---

<a id="sec-14"></a>
## 4. Analytik, Nasschemische Nachweise & Instrumentelle Strukturaufklärung

<a id="sec-15"></a>
### 4.1 Schmelzpunkt (`mp`), Mischschmelzpunkt & Klassische Nasschemische Nachweise (LibreTexts Kapitel 6)

#### A. Schmelzpunkt (`Melting Point`, LibreTexts 6.01)
- **Qualitätsgesetze:**
  1. Reinstoffe zeigen ein enges Schmelzintervall ($\Delta T \le \mathbf{1\text{--}2\,^\circ\text{C}}$).
  2. **Schmelzpunktdepression durch Verunreinigungen:** Verunreinigungen **senken** den Schmelzpunkt und **verbreitern** das Intervall deutlich ($\Delta T > 4\text{--}10\,^\circ\text{C}$). *(Ausnahme: Eutektische Gemische schmelzen zwar scharf, aber deutlich unterhalb des Reinstoff-Schmelzpunkts!)*
  3. **Mischschmelzpunkt (`Mixed Melting Point`):** Um eine unbekannte Substanz zu identifizieren, mischt man sie $1:1$ mit einer authentischen Referenzprobe: Bleibt der Schmelzpunkt unverändert und scharf $\rightarrow$ **identisch**; sinkt und verbreitert sich der Schmelzpunkt $\rightarrow$ **verschieden**!
  4. **Heizrate:** In der Nähe des erwarteten Schmelzpunkts (ab $15\,^\circ\text{C}$ darunter) maximal **$1\text{--}2\,^\circ\text{C/min}$** aufheizen; stets nur trockene, fein verriebene Proben ($1\text{--}2\text{ mm}$ Füllhöhe in der Kapillare) messen und einmal geschmolzene Proben **niemals** ein zweites Mal verwenden (Zersetzungsgefahr!).

#### B. Vollständige Tabelle der Klassischen Nasschemischen Funktionsgruppen-Nachweise (LibreTexts 6.04)

| Nachweis-Test | Exakte Reagenz-Zusammensetzung & Durchführung | Positives Ergebnis (Farbe / Niederschlag / Gas) | Erfasste Substrate vs. Negative / Fehlerquellen (`Pitfalls`) |
| :--- | :--- | :--- | :--- |
| **pH- & Natriumhydrogencarbonat-Test** | $2\text{ mL } 5\,\%\text{ NaHCO}_3\text{(aq)} + 5\text{ Tropfen / } 50\text{ mg}$ Probe; parallel wässrige Lösung auf blaues Lackmus- oder pH-Papier. | **Kräftige $\text{CO}_2$-Gasentwicklung (Bläschen / Schäumen)** und $\text{pH} < 5$. | **Positiv:** Carbonsäuren ($\text{p}K_\text{S}\sim 4\text{--}5$), Sulfonsäuren.<br>**Negativ:** Phenole ($\text{p}K_\text{S}\sim 10$, saurer als Alkohol, aber kein $\text{CO}_2$ mit $\text{NaHCO}_3$!), Alkohole. |
| **Eisen(III)-chlorid-Test ($\text{FeCl}_3$)** | Probe in EtOH/$\text{H}_2\text{O}$ + $2\text{ Tropfen } 1\text{--}5\,\%\,\text{FeCl}_3$-Lösung. | **Intensive blaue, violette, rote oder tiefgrüne Komplex-Färbung** (Negativ = blassgelbe Reagenzfarbe). | **Positiv:** **Phenole** ($\text{Ar-OH}$) und ausgeprägte **Enole** (1,3-Diketone, $\beta$-Ketoester). *(Sterisch stark gehinderte Phenole wie 2,6-Di-*tert*-butylphenol können negativ bleiben!).* |
| **Brom-Test ($\text{Br}_2$ in $\text{DCM}$)** | $4\text{ Tropfen / } 50\text{ mg}$ Probe in $1\text{ mL DCM}$ oder $\text{DME}$ + $2\text{ Tropfen}$ orangefarbene **$5\,\%\,\text{Br}_2/\text{DCM}$**. | **Sofortige Entfärbung** der orangen Bromlösung nach farblos (ohne $\text{HBr}$-Nebel!). | **Positiv:** **Alkene, Alkine** (sofortige elektrophile Addition). *(Gesättigte Aldehyde entfärben verzögert nach $\sim 1\text{ min}$ unter $\text{HBr}$-Bildung).* **Negativ:** Aromaten (unterscheiden Alken vs. Aren!). |
| **Baeyer-Test ($\text{KMnO}_4$)** | $4\text{ Tropfen / } 40\text{ mg}$ Probe in $1\text{ mL EtOH}$ oder $\text{DME}$ + $3\text{ Tropfen}$ tiefviolettes $1\,\%\,\text{KMnO}_4\text{(aq)}$. | **Entfärbung der violetten Lösung + brauner $\text{MnO}_2$-Niederschlag** innerhalb $1\text{ min}$. | **Positiv:** **Alkene, Alkine**, leicht oxidierbare **Aldehyde** (und manche $1^\circ/2^\circ$-Alkohole/Phenole). **Negativ:** Aromaten, Ester, Ketone, Carbonsäuren. *(Reines $\text{EtOH}$ als Lösungsmittel reagiert langsam nach längerer Zeit $\rightarrow$ Vergleichsblindprobe machen!).* |
| **Chromsäure- / Jones-Test** | $2\text{ Tropfen / } 20\text{ mg}$ Probe in $1\text{ mL Aceton}$ + $2\text{ Tropfen}$ oranges **$\text{CrO}_3/\text{H}_2\text{SO}_4/\text{H}_2\text{O}$** (*hochgiftig, Handschuhe!*). | **Sofortiger Farbumschlag von Orangerot nach Blaugrün/Dunkelgrün ($\text{Cr}^{3+}$)** + Niederschlag. | **Positiv:** **$1^\circ$- und $2^\circ$-Alkohole**, **Aldehyde**.<br>**Negativ:** **$3^\circ$-Alkohole**, Ketone, Ester, Ether, Aromaten! |
| **Lucas-Test ($\text{HCl} / \text{ZnCl}_2$)** | $2\text{ mL}$ **Lucas-Reagenz** ($160\text{ g wasserfreies }\text{ZnCl}_2$ in $100\text{ mL kalter konz. HCl}$) + $5\text{ Tropfen}$ Alkohol (max. $\le C_6$-Alkohole, müssen sich anfangs lösen!). | **Weiße Trübung oder Abscheidung einer zweiten unlöslichen Alkylchlorid-Schicht ($\text{R-Cl}$)**:<br>• **Sofort ($<1\text{ min}$):** **$3^\circ$-, Allyl- oder Benzylalkohol**.<br>• **$5\text{--}10\text{ min}$ (oder gelinde Wärme):** **$2^\circ$-Alkohol**.<br>• **Keine Trübung:** **$1^\circ$-Alkohol**! | Klassifiziert **$1^\circ$ vs. $2^\circ$ vs. $3^\circ$/Benzyl-Alkohole** über die $S_\text{N}1$-Carbokation-Stabilität (**ergänzt den Jones-Test**: Jones trennt $1^\circ/2^\circ$ von $3^\circ$; Lucas trennt $3^\circ$ [$<1\text{ min}$] vs. $2^\circ$ [$5\text{ min}$] vs. $1^\circ$ [negativ]!). |
| **2,4-DNPH (Brady-Test)** | $3\text{ Tropfen / } 10\text{ mg}$ Probe in wenig EtOH + $1\text{ mL}$ **2,4-Dinitrophenylhydrazin-Reagenz** ($\text{H}_2\text{SO}_4/\text{EtOH}/\text{H}_2\text{O}$). | **Sofortige Bildung eines voluminösen Niederschlags**:<br>• **Gelb-Orange:** Nicht-konjugierter Aldehyd/Keton.<br>• **Tiefrot:** Konjugierter ($\alpha,\beta$-Enon/Aryl) Aldehyd/Keton! | **Positiv:** Nahezu alle **Aldehyde und Ketone**.<br>**Negativ:** Carbonsäuren, Ester, Amide, Alkohole. *(Schmelzpunkt des abfiltrierten, umkristallisierten 2,4-DNP-Hydrazons dient zur Derivatisierungs-Identifikation!).* |
| **Tollens-Test (Silberspiegel)** | $1\text{ mL } 5\,\%\,\text{AgNO}_3 + 1\text{ mL } 10\,\%\,\text{NaOH}$ ($\rightarrow$ braunes $\text{Ag}_2\text{O}$), tropfenweise konz. $\text{NH}_4\text{OH}$ bis gerade wieder klar ($[\text{Ag(NH}_3)_2]^+$) + $3\text{ Tropfen}$ Probe (kurz $50\,^\circ\text{C}$ Wasserbad). | **Metallischer Silberspiegel an der Glaswand** oder feiner schwarzer $\text{Ag}^0$-Niederschlag! | **Positiv:** **Aldehyde** (auch $\alpha$-Hydroxyketone und reduzierende Zucker!). **Negativ:** Ketone, Alkohole, Ester.<br>**KRITISCHES SICHERHEITSGESETZ:** Tollens-Reagenz bildet beim Stehenlassen hochexplosives **Silberfulminat / Silbernitrid ($\text{Ag}_3\text{N}$)**! Sofort nach dem Test mit **$5\,\%\,\text{HCl}$ ansäuern** und verwerfen – niemals lagern! |
| **Benedict- & Fehling-Test** | $\text{CuSO}_4 + \text{Na-Citrat} + \text{Na}_2\text{CO}_3$ (tiefblau, alkalisch; bzw. Tartrat bei Fehling) + Probe, $3\text{ min}$ im kochenden Wasserbad erhitzen. | **Ziegelroter $\text{Cu}_2\text{O}$-Niederschlag** (über grün/gelb/orange). | **Positiv:** **Aliphatische Aldehyde** und **reduzierende Zucker** (Aldosen, $\alpha$-Hydroxyketone). **Negativ:** **Aromatische Aldehyde (z. B. Benzaldehyd!)** und normale Ketone! |
| **Iodoform-Test ($\text{I}_2 / \text{KI} / \text{NaOH}$)** | Probe in $\text{H}_2\text{O}$ oder $\text{DME}$ + $10\,\%\text{ NaOH}$ + $\text{I}_2/\text{KI}$-Lösung ($10\text{ g KI} + 5\text{ g I}_2$ in $100\text{ mL H}_2\text{O}$) im Überschuss bis braun, kurz $60\,^\circ\text{C}$ wärmen, überschüssiges $\text{I}_2$ mit NaOH entfärben. | **Blaßgelber, charakteristisch medizinisch riechender Niederschlag von Iodoform ($\text{CHI}_3$, $\text{mp } 119\,^\circ\text{C}$)**. | **Positiv:** **Methylketone ($\text{R-CO-CH}_3$)**, Acetaldehyd, Ethanol und **2-Alkanole ($\text{R-CH(OH)-CH}_3$)**! **Fehlalarm-Warnung:** Niemals Testgläser mit **Aceton** spülen und nicht vollständig trocknen – Aceton-Spuren geben sofort ein falsch-positives Ergebnis! |
| **Eisenhydroxamat-Test (Ester-Test)** | **Vorprobe** ($1\text{ mL EtOH} + \text{Probe} + \text{HCl} + \text{FeCl}_3$: muss gelb bleiben, um Enol/Phenol auszuschließen!), dann Hauptprobe mit $\text{NH}_2\text{OH}\cdot\text{HCl} + 6\,\text{M NaOH}$ ($3\text{ min}$ kochen), kühlen, $1\,\text{M HCl} + \text{FeCl}_3$. | **Tief weinrote / burgunderrote Färbung** (Eisen(III)-hydroxamat-Komplex). | **Positiv:** **Carbonsäureester** und **Lactone** (Anhydride und Säurechloride reagieren ebenfalls). |
| **Silbernitrat-Test ($\text{AgNO}_3/\text{EtOH}$, $S_\text{N}1$) vs. Finkelstein-Test ($\text{NaI/Aceton}$, $S_\text{N}2$)** | **$\text{AgNO}_3$:** $2\text{ mL } 1\,\%\,\text{AgNO}_3\text{ in EtOH} + 4\text{ Tropfen}$ Halogenid (RT, ggf. erwärmen).<br>**$\text{NaI}$:** $2\text{ mL } 15\,\%\,\text{NaI in trockenem Aceton} + 4\text{ Tropfen}$ Chlorid/Bromid (RT $\rightarrow 50\,^\circ\text{C}$). | • **$\text{AgNO}_3$:** Weißer/cremefarbener/gelber **$\text{AgX}$-Niederschlag** ($\text{I} > \text{Br} > \text{Cl}$; **Allyl/Benzyl/$3^\circ$ sofort bei RT**; $2^\circ$ langsam; $1^\circ$ erst beim Erwärmen; **Aryl/Vinyl negativ!**).<br>• **$\text{NaI/Aceton}$:** Weißer **$\text{NaCl}/\text{NaBr}$-Niederschlag** ($1^\circ$ sofort bei RT; $2^\circ$ bei $50\,^\circ\text{C}$; **$3^\circ$/Aryl/Vinyl negativ!**). | **Komplementäre Halogenid-Klassifizierung:** Kombiniert trennen beide Tests **$1^\circ$** ($\text{NaI}$ schnell, $\text{AgNO}_3$ langsam), **$2^\circ$** (beide moderat), **$3^\circ$/Allyl/Benzyl** ($\text{AgNO}_3$ sofort, $\text{NaI}$ bei $3^\circ$ negativ!) und **Aryl-/Vinylhalogenide** (beide negativ!). |

---

<a id="sec-16"></a>
### 4.2 Infrarot- (`IR`) & Raman-Spektroskopie (inkl. Spektroskopie-Praxisregeln)

> **Spektroskopische Praxisregeln (`spectroscopist`):**
> - **Kalibrierung:** IR-Spektrometer gegen die Polystyrol-Bande bei **$1601\text{ cm}^{-1}$** kalibrieren.
> - **ATR vs. KBr-Pressling:** Bei **ATR-FTIR** Anpressdruck, Kristalltyp (Diamant/ZnSe) und Eindringtiefen-Korrektur beachten (längere Wellenlängen dringen tiefer ein $\rightarrow$ Banden bei kleineren $\tilde{\nu}$ erscheinen im unkorrigierten ATR-Spektrum intensiver als in Transmission!). Bei wässrigen Puffern führt Pfadlängen-Mismatch bei der Subtraktion zu **ableitungsförmigen Artefakten**!
> - **Fermi-Resonanz (wichtiger Fallstrick!):** Zwei Banden entstehen durch Kopplung einer Grundschwingung mit einem Oberton gleicher Symmetrie, z. B. das charakteristische **„Aldehyd-Dublett“** ($\nu_{\text{C-H}}$ des Aldehyds spaltet in zwei Banden bei **$2720\text{ cm}^{-1}$ und $2820\text{ cm}^{-1}$** auf!) oder die **Carbonsäureanhydrid-Doppelbande** ($1815$ und $1750\text{ cm}^{-1}$)!

| Funktionelle Gruppe / Schwingung | Wellenzahl $\tilde{\nu}$ ($\text{cm}^{-1}$) | Intensität & Bandenform | Diagnostische Effekte (H-Brücken, Konjugation, Ringspannung!) |
| :--- | :---: | :--- | :--- |
| **$\text{O-H}$ (freier Alkohol/Phenol, verdünnt)** | $3650\text{--}3590$ | Scharf, mittel | Ohne Wasserstoffbrücken (in verdünnter $\text{CCl}_4$-Lösung). |
| **$\text{O-H}$ (H-verbrückter Alkohol/Phenol)** | **$3550\text{--}3200$** | **Stark, breit, abgerundet** | Zentrum meist um $3300\text{ cm}^{-1}$; in konzentrierter Substanz/Film stets breit. |
| **$\text{O-H}$ (Carbonsäure, Dimer)** | **$3300\text{--}2500$** | **Extrem breit („Bärtige Bande“)** | Überlappt komplett mit der C-H-Streckschwingungsregion um $3000\text{ cm}^{-1}$! |
| **$\text{N-H}$ ($1^\circ$-Amin / $1^\circ$-Amid)** | $3500\text{--}3300$ | **2 Banden (Dublett)**, mittel | Symmetrische und antisymmetrische $\text{NH}_2$-Streckschwingung! |
| **$\text{N-H}$ ($2^\circ$-Amin / $2^\circ$-Amid / Indol)** | $3450\text{--}3300$ | **1 Bande (Singulett)**, mittel | **$3^\circ$-Amine ($\text{NR}_3$) haben KEINE N-H-Bande!** |
| **$\equiv\text{C-H}$ (Terminales Alkin, $sp$)** | **$3330\text{--}3270$** | **Stark, sehr SCHARF** | Deutlich schmaler und schärfer als eine $\text{O-H}$-Bande bei $3300\text{ cm}^{-1}$! |
| **$=\text{C-H}$ (Alken / Aromat, $sp^2$)** | **$3100\text{--}3000$** | Mittel, oft Schulter | **Kritische Grenzlinie $3000\text{ cm}^{-1}$:** $>3000 = sp^2\text{-CH}$; $<3000 = sp^3\text{-CH}$! |
| **$-\text{C-H}$ (Alkan, $sp^3$)** | **$2980\text{--}2850$** | Stark–mittel, strukturiert | $-\text{CH}_3$ ($2960, 2870$), $-\text{CH}_2-$ ($2925, 2850$). |
| **Aldehyd $-\text{C(=O)-H}$ (Fermi-Dublett!)** | **$2830\text{--}2810$ & $2740\text{--}2710$** | **Mittel, zwei scharfe Spitzen** | Beweist ein Aldehyd-Proton zusätzlich zur $\text{C=O}$-Bande! |
| **$\text{C}\equiv\text{N}$ (Nitril) / $\text{C}\equiv\text{C}$ (Alkin)** | **$2260\text{--}2210$ / $2260\text{--}2100$** | Mittel–stark ($\text{CN}$) / schwach ($\text{C}\equiv\text{C}$) | Symmetrische interne Alkine sind IR-inaktiv (**Raman-aktiv!**). Konjugierte Nitrile sinken auf $\sim 2225\text{ cm}^{-1}$. |
| **Kumulene ($\text{N=C=O}$, $\text{N}_3$, $\text{C=C=O}$)** | $2275\text{--}2100$ | **Extrem stark** | Isocyanat $2270$, Azid $-\text{N}_3$ **$2160\text{--}2090$**, Keten $2150\text{ cm}^{-1}$. |
| **Säurechlorid ($\text{R-CO-Cl}$)** | **$1815\text{--}1785$** | Sehr stark | Starker $-I$-Effekt von $\text{Cl}$ erhöht Kraftkonstante von $\text{C=O}$. |
| **Anhydrid ($\text{R-CO-O-CO-R}$)** | **$1830\text{--}1800$ & $1775\text{--}1740$** | **2 starke Banden** ($\Delta\tilde{\nu} \approx 60\text{ cm}^{-1}$) | Gekoppelte symmetrische & antisymmetrische Schwingung (bei cyclischen 5-Ring-Anhydriden bis $1865 / 1785\text{ cm}^{-1}$!). |
| **Ester ($\text{R-CO}_2\text{R}'$) & Lactone** | **$1750\text{--}1735$** (acyclisch) | Sehr stark | **Ringspannung:** $\delta$-Lacton (6-Ring) $\mathbf{1735}$; **$\gamma$-Lacton (5-Ring) $\mathbf{1770\text{--}1780}$**; $\beta$-Lacton (4-Ring) $\mathbf{1820\text{ cm}^{-1}}$! **Konjugation** ($\alpha,\beta$-ungesättigt/Benzoat) senkt um $20\text{ cm}^{-1}$ auf $\mathbf{1720\text{ cm}^{-1}}$! |
| **Aldehyd ($\text{R-CHO}$) & Keton ($\text{R}_2\text{C=O}$)** | **$1740\text{--}1720$** / **$1725\text{--}1705$** | Sehr stark | **Konjugation** (Enon/Arylketon): sinkt auf **$1700\text{--}1680\text{ cm}^{-1}$**! **Ringspannung:** Cyclohexanon **$1715$**, Cyclopentanon **$1745$**, Cyclobutanon **$1780$**, Cyclopropanon **$1815\text{ cm}^{-1}$**! |
| **Carbonsäure ($\text{R-CO}_2\text{H}$)** | **$1720\text{--}1700$** (Dimer) | Sehr stark | Konjugierte Säure: $1700\text{--}1680\text{ cm}^{-1}$. (Carboxylat $-\text{CO}_2^-$: $1610\text{--}1550$ & $1420\text{--}1300\text{ cm}^{-1}$). |
| **Amid ($\text{R-CONR}'_2$)** | **$1680\text{--}1630$** (**Amid I**) | Sehr stark | Starke $+M$-Resonanz senkt die $\text{C=O}$-Bindungsordnung! ($\beta$-Lactam = **$1760\text{--}1730\text{ cm}^{-1}$** wegen fehlender Resonanz + Ringspannung!). $2^\circ$-Amide zeigen zusätzlich **Amid II ($\text{N-H}$-Beugung) bei $1570\text{--}1515\text{ cm}^{-1}$**! |
| **$\text{C=C}$ (Alken / Enon) & Aromaten-Gerüst** | $1680\text{--}1620$ / **$1600, 1580, 1500, 1450$** | Mittel–schwach | Enolether/Enamine sind intensiv bei $1650\text{--}1610\text{ cm}^{-1}$. |
| **Nitrogruppe ($\text{R-NO}_2$)** | **$1560\text{--}1515$ & $1385\text{--}1345$** | **2 sehr starke Banden** | Antisymmetrische und symmetrische $\text{NO}_2$-Streckschwingung. |
| **Sulfon ($\text{R}_2\text{SO}_2$) / Sulfonamid / Tosylat** | $1350\text{--}1300$ & $1160\text{--}1120$ | **2 sehr starke Banden** | Sehr charakteristisch zur Verfolgung von Tosylierungen/Mesylierungen! |
| **$\text{C-O}$ (Ester, Ether, Alkohol) / $\text{C-F}$** | $1300\text{--}1000$ | Stark | Ester zeigen 2 starke Banden bei $\sim 1250$ & $1050\text{ cm}^{-1}$ (`Rule of Three`: 1740, 1250, 1050). |
| **Aromaten-$\text{C-H}$ `oop`-Schwingungen (Substitutionsmuster!)** | **$900\text{--}675$** | Stark | **Monosubst.:** $750$ + $700$; **1,2-*ortho*:** $750$ (1 Bande); **1,3-*meta*:** $880 + 780 + 690$; **1,4-*para*:** **$830\text{--}810$** (1 starke Bande)! |

---

<a id="sec-17"></a>
### 4.3 $^1\text{H}$- und $^{13}\text{C}$-NMR-Spektroskopie, Restlösungsmittel & `nmrglue`-Prozessierung

#### A. Vollständige Tabelle der Deuterierten NMR-Lösungsmittel & Häufigsten Labor-Verunreinigungen ($\delta$ in ppm, nach Gottlieb/Fulmer)

| Lösungsmittel / Labor-Verunreinigung | $^1\text{H}$-NMR-Restsignal ($\delta$ in ppm, Multiplizität, $J_{\text{HD}}$) | $^{13}\text{C}$-NMR-Solvent-Signal ($\delta$ in ppm, Multiplizität) | $\text{H}_2\text{O}$-Signal ($\delta$ in ppm) | Typische Labor-Kontaminationen in $\text{CDCl}_3$ ($\delta_\text{H}$ / $\delta_\text{C}$ in ppm) |
| :--- | :--- | :--- | :---: | :--- |
| **Chloroform-$d_1$ ($\text{CDCl}_3$)** *(mit $0.03\,\%$ TMS)* | **$7.26$ (s)** *(Standard!)* | **$77.16$ (t, $J = 32\text{ Hz}$)** | **$1.56$ (s)** *(variabel!)* | • **Silikonfett (`Grease`):** $0.07\text{ (s)}$ / $1.0\text{ ppm}$<br>• **H-Fett / Mineralöl (`NaH`):** $0.88\text{ (t)}, 1.26\text{ (m)}$<br>• **Aceton:** $2.17\text{ (s)}$ / $30.9, 207.1$<br>• **$\text{EtOAc}$:** $1.26\text{ (t)}, 2.05\text{ (s)}, 4.12\text{ (q)}$<br>• **$\text{DCM}$:** $5.30\text{ (s)}$ / $53.5$<br>• **$\text{Et}_2\text{O}$:** $1.21\text{ (t)}, 3.48\text{ (q)}$<br>• **Hexan:** $0.88\text{ (t)}, 1.26\text{ (m)}$<br>• **$\text{THF}$:** $1.85\text{ (m)}, 3.76\text{ (m)}$<br>• **$\text{MeOH}$:** $3.49\text{ (s)}$ / $50.4$<br>• **$\text{DMF}$:** $2.88\text{ (s)}, 2.96\text{ (s)}, 8.02\text{ (s)}$<br>• **$\text{DMSO}$:** $2.62\text{ (s)}$<br>• **Toluol:** $2.36\text{ (s)}, 7.15\text{--}7.25\text{ (m)}$<br>• **$\text{Et}_3\text{N}$:** $1.03\text{ (t)}, 2.53\text{ (q)}$<br>• **BHT (aus $\text{THF}$-Stabilisator!):** $1.43\text{ (s, 18H)}, 2.27\text{ (s, 3H)}, 5.01\text{ (s, 1H)}, 6.98\text{ (s, 2H)}$ |
| **$\text{DMSO-}d_6$ ($(\text{CD}_3)_2\text{SO}$)** | **$2.50$ (quin, $J = 1.9\text{ Hz}$)** | **$39.52$ (hept)** | **$3.33$ (s, oft breit)** | $\text{DMSO-}d_6$ trennt diastereotope Signale/Rotamere durch H-Brücken; **$\text{OH/NH}$-Protonen zeigen in trockenem $\text{DMSO-}d_6$ scharfe Kopplungen (`t` für $1^\circ$-ROH, `d` für $2^\circ$-ROH, `s` für $3^\circ$-ROH!)**! |
| **Methanol-$d_4$ ($\text{CD}_3\text{OD}$)** | **$3.31$ (quin)** *(+ $\text{OD/OH}$ bei $4.87$)* | **$49.00$ (hept)** | **$4.87$ (s)** | **Achtung:** Acide $\text{OH, NH, SH, CO}_2\text{H}$-Protonen tauschen in $\text{CD}_3\text{OD}$ und $\text{D}_2\text{O}$ komplett gegen Deuterium aus und **verschwinden** aus dem $^1\text{H}$-NMR! |
| **Aceton-$d_6$ ($(\text{CD}_3)_2\text{CO}$)** | **$2.05$ (quin)** | **$29.84$ (hept), $206.26$ (s)** | **$2.84$ (s)** | Neutral, säurefrei (ideal für säureempfindliche Gruppen, falls $\text{CDCl}_3$ durch $\text{HCl}$-Spuren zersetzt – **Hinweis:** $\text{CDCl}_3$ für Acetale/Enolether stets vorher über basisches $\text{Al}_2\text{O}_3$ oder festes $\text{K}_2\text{CO}_3$ filtrieren!). |
| **Benzol-$d_6$ ($\text{C}_6\text{D}_6$)** | **$7.16$ (s)** | **$128.06$ (t)** | **$0.40$ (s)** | Säurefrei! Durch starken **ASIS-Effekt** (`Aromatic Solvent-Induced Shift`) trennt $\text{C}_6\text{D}_6$ oft überlagerte Multipletts, die in $\text{CDCl}_3$ zusammenfallen! |
| **$\text{D}_2\text{O}$** *(Referenz DSS $= 0\text{ ppm}$)* | **$4.79$ (s)** | *(kein C; interner Standard nötig)* | **$4.79$ (s)** | Für wasserlösliche Salze, Aminosäuren, Kohlenhydrate. |

#### B. Chemische Verschiebungen ($^1\text{H}$ & $^{13}\text{C}$) und Kopplungskonstanten ($J$ in Hz)

| Struktureinheit / Protonen- & Kohlenstofftyp | $^1\text{H}$-NMR $\delta$ (ppm) | $^{13}\text{C}$-NMR $\delta$ (ppm) | Diagnostische Kopplungen ($^nJ$ in Hz) & Spezialregeln |
| :--- | :---: | :---: | :--- |
| **$\text{R-CH}_3$ / $\text{R}_2\text{CH}_2$ / $\text{R}_3\text{CH}$ (Alkyl)** | $0.85\text{--}1.0 \;/\; 1.2\text{--}1.4 \;/\; 1.4\text{--}1.7$ | $10\text{--}25 \;/\; 22\text{--}38 \;/\; 28\text{--}50$ | **$^3J_{\text{vic}}$ (frei drehbar):** $6.5\text{--}7.5\text{ Hz}$. **Karplus-Gleichung (Cyclohexan/Bicyclus):** $^3J_{\text{ax-ax}}$ ($180^\circ$) $= \mathbf{8\text{--}13\text{ Hz}}$; $^3J_{\text{ax-eq}}$ / $^3J_{\text{eq-eq}}$ ($60^\circ$) $= \mathbf{2\text{--}5\text{ Hz}}$! |
| **Allylisch ($\text{C=C-CH}_x$) / Benzylisch ($\text{Ar-CH}_x$)** | $1.6\text{--}2.2 \;/\; 2.2\text{--}2.9$ | $18\text{--}35 \;/\; 20\text{--}45$ | Allyl-Kopplung $^4J_{\text{H-C=C-CH}} = \mathbf{1\text{--}2\text{ Hz}}$ (W-Kopplung!). |
| **$\alpha$ zu Carbonyl ($\text{CH}_x\text{-C=O}$) / $\alpha$ zu Amin ($\text{CH}_x\text{-NR}_2$)** | $2.0\text{--}2.6 \;/\; 2.2\text{--}3.0$ | $30\text{--}50 \;/\; 40\text{--}65$ | $\alpha$-C neben Amid-$\text{N}$ liegt tiefer ($3.1\text{--}3.6\text{ ppm}$). |
| **Terminales Alkin ($\text{R-C}\equiv\text{C-H}$) / Alkin-C** | **$1.8\text{--}3.1$** | **$65\text{--}90$** *(zwischen Alkan und Alken!)* | Anisotropie-Kegel des Alkins schirmt das $sp$-$\text{H}$ ab! |
| **$\text{CH}_x\text{-Halogen}$ ($\text{I}, \text{Br}, \text{Cl}, \text{F}$) / $\text{CH}_x\text{-O}$ (Alkohol/Ether/Ester)** | $\text{I}: 3.1 \;/\; \text{Br}: 3.4 \;/\; \text{Cl}: 3.6 \;/\; \text{O}: \mathbf{3.3\text{--}4.5}$ *(Ester $\text{CH-OCOR}$ bei $4.0\text{--}5.2$!)* | $5\text{--}40\text{ (I/Br/Cl)} \;/\; \mathbf{50\text{--}85\text{ (C-O)}}$ | Fluor-Kopplungen: $^2J_{\text{H-F}} \approx \mathbf{45\text{--}55\text{ Hz}}$, $^3J_{\text{H-F}} \approx 10\text{--}25\text{ Hz}$, $^1J_{\text{C-F}} \approx \mathbf{165\text{--}280\text{ Hz}}$! |
| **Acetal-Proton / Anomeres Zucker-$\text{H}(1)$ ($\text{O-CH-O}$)** | **$4.5\text{--}5.8$** | **$95\text{--}110$** | Bei Pyranosiden: $\alpha$-anomeres $\text{H}(1)_{\text{eq}}$ bei $\sim 5.0\text{ ppm}$ (**$^3J_{1,2} \approx 3.5\text{ Hz}$**); $\beta$-anomeres $\text{H}(1)_{\text{ax}}$ bei $\sim 4.4\text{ ppm}$ (**$^3J_{1,2} \approx 8.0\text{ Hz}$**)! |
| **Olefinisches $\text{C=C-H}$ (Alken / Enon)** | **$4.6\text{--}6.5$** *($\beta$-H von Enon bis $7.5$!)* | **$105\text{--}150$** | **Goldenes $(E)$ vs. $(Z)$-Gesetz:**<br>• **$^3J_{\textit{trans}\text{ (E)}} = \mathbf{12\text{--}18\text{ Hz}}$** *(Standard $\sim 15\text{--}16\text{ Hz}$)*<br>• **$^3J_{\textit{cis}\text{ (Z)}} = \mathbf{6\text{--}12\text{ Hz}}$** *(Standard $\sim 9\text{--}11\text{ Hz}$)*<br>• **$^2J_{\text{gem}} (\text{=CH}_2) = \mathbf{0\text{--}3\text{ Hz}}$**! |
| **Aromatisches $\text{Ar-H}$ / Heteroaryl-H** | **$6.5\text{--}8.5$** *(Pyridin $\text{H}(2)$: $\sim 8.6$)* | **$110\text{--}160$** | **$^3J_{\textit{ortho}} = 7.0\text{--}9.0\text{ Hz}$**; **$^4J_{\textit{meta}} = 1.2\text{--}3.0\text{ Hz}$**; $^5J_{\textit{para}} = 0\text{--}1\text{ Hz}$. **1,4-disubstituiertes Benzol:** symmetrisches **$\text{AA}'\text{BB}'$-Dublett-Paar** (je 2H)! |
| **Aldehyd $-\text{CH=O}$** | **$9.4\text{--}10.2$** | **$190\text{--}205$** | $^3J_{\text{H-CH=O}} \approx 1\text{--}3\text{ Hz}$. |
| **Carbonsäure $-\text{CO}_2\text{H}$ / Enol-$\text{OH}$** | **$10.5\text{--}13.5$** *(Enol bis $16\text{ ppm}$)* | **$170\text{--}185$** | Sehr breit (H-Austausch), verschwindet beim **$\text{D}_2\text{O}$-Shake**! |
| **Keton / Ester / Amid $\text{C=O}$ ($^{13}\text{C}$)** | — | **Keton: $200\text{--}220$**; **Ester/Amid/Lacton: $165\text{--}178$** | **DEPT-135-Regel:** **$\text{CH}_3$ & $\text{CH}$ = POSITIV (nach oben)**; **$\text{CH}_2$ = NEGATIV (nach unten)**; **quartäre $\text{C}_\text{q}$ (inkl. $\text{C=O}$) = ABWESEND**! (DEPT-90 zeigt nur $\text{CH}$). |

#### C. 2D-NMR-Zuordnungs-Strategie & `nmrglue`-Prozessierungs-Guardrails
- **Systematische Strukturaufklärung (2D-Workflow):**
  1. **$^{13}\text{C}$ + DEPT-135 + HRMS:** Exakte Atomzahl, RDBE und Anzahl an $\text{CH}_3, \text{CH}_2, \text{CH}, \text{C}_\text{q}$ bestimmen.
  2. **Multiplizitäts-editiertes `HSQC` ($^1J_{\text{CH}}$):** Ordnet jedes Proton direkt seinem gebundenen $^{13}\text{C}$-Atom zu und trennt sofort $\text{CH}_2$ (negativ/blau) von $\text{CH}/\text{CH}_3$ (positiv/rot).
  3. **`COSY` / `TOCSY` ($^3J_{\text{HH}}$):** Verknüpft die protonentragenden Spin-Systeme entlang durchgehender C-C-Ketten.
  4. **`HMBC` ($^2J_{\text{CH}}$ und $^3J_{\text{CH}}$, optimiert auf $J \approx 8\text{ Hz}$):** Überbrückt quartäre Kohlenstoffe, Heteroatome ($\text{O, N, S}$) und Carbonylgruppen – **Achtung:** $^2J$ vs. $^3J$ vs. gelegentliche $^4J$ (W-Kopplung in Aromaten) können überlappen!
  5. **`NOESY` / `ROESY` (räumlicher Dipol-Abstand $<4\text{--}5\text{ Å}$):** Bestimmt $(E/Z)$-Doppelbindungsgeometrien, relative Konfiguration (*syn/anti*, axial/äquatorial) und Konformation.
  6. **Spezifische NMR-Störungen:** Verbreiterung/Doppelsignale prüfen auf **Rotamere** (Amide/Carbamate $\rightarrow$ **Hochtemperatur-NMR in $\text{DMSO-}d_6$ bei $80\text{--}100\,^\circ\text{C}$** zur Koaleszenz!), **Atropisomere**, **paramagnetische Metallspuren** ($\rightarrow$ Evans-Methode / Chelex-Filtration) oder **TFA-Salz-Verbreiterung**.
- **`nmrglue`-Prozessierungsregeln für rohe 1D-FIDs:**
  - `SW` (Hz), `OBS` (MHz), Carrier (ppm) und Vorzeichenkonvention (`-i` vs. `+i`) explizit dokumentieren; Bruker-`remove_digital_filter` **niemals zweimal** anwenden (Phase wird zerstört!).
  - Zero Filling verbessert nur die Interpolation, **nicht** die spektrale Auflösung; `em`-Linienverbreiterung erwartet $\Delta\nu / \text{SW}$.
  - Phase (`phase0 + phase1 * idx / N`) stets sowohl am **Real- als auch am Imaginärkanal** kontrollieren; lineare/polynomielle Baseline **nur** auf explizit signalfreien Regionen fitten (Polynom-Baselines erfinden sonst künstliche Peaks!); negative Integralflächen **nie** mit `abs()` verdecken, sondern als diagnostisches Phasen-/Baseline-Warnsignal bewahren!

---

<a id="sec-18"></a>
### 4.4 Massenspektrometrie (`MS`, `HRMS`, `MS/MS`), Fragmentierung, `matchms`/`pyOpenMS` & Methodenvalidierung

#### A. Summenformel-Gesetze, RDBE, Stickstoffregel & Isotopenmuster (`mass-spectrometrist`)
1. **Rings-and-Double-Bonds Equivalent (`RDBE` / `DBE`, Doppelbindungsäquivalente):**
   Für eine neutrale Summenformel $\text{C}_c\text{H}_h\text{N}_n\text{O}_o\text{Hal}_x$:
   $$\text{RDBE} = c - \frac{h + x}{2} + \frac{n}{2} + 1$$
   *(Zweiwertige Atome wie $\text{O}, \text{S}$ tragen $0$ bei; $\text{P}$ zählt wie $\text{N}$ +$\frac{n}{2}$; $\text{Si}$ zählt wie $\text{C}$. Ein gerades elektronisches Kation wie $[\text{M}+\text{H}]^+$ hat bei dieser Formel für das Ion selbst eine **halbzahlige** $\text{RDBE}$ wie $X.5$; nach Abzug von $\text{H}^+$ für das neutrale Molekül $M$ muss $\text{RDBE}$ stets eine **ganze Zahl $\ge 0$** sein! Benzolring: $\text{RDBE} = 4$; $\text{C=O}/\text{C=C}$: $1$; $\text{C}\equiv\text{C}/\text{C}\equiv\text{N}$: $2$).*
2. **Die Stickstoffregel (`Nitrogen Rule`):**
   - Ein neutrales Molekül aus $\text{C, H, N, O, S, Hal}$ hat eine **UNGERADE nominelle Molmasse $M$** genau dann, wenn es eine **UNGERADE Anzahl an Stickstoffatomen ($1, 3, 5, \dots$)** enthält; eine **GERADE Molmasse $M$** bedeutet **$0$ oder eine GERADE Anzahl an $\text{N}$-Atomen ($0, 2, 4, \dots$)**!
   - *(**ESI-Korrektur!** Da ESI $[M+\text{H}]^+$ misst, gilt für das $[M+\text{H}]^+$-Ion genau das Umgekehrte: Ein **gerades** $m/z$ für $[M+\text{H}]^+$ bedeutet eine **ungerade** Stickstoffzahl $1, 3, 5\dots$!)*
3. **Diagnostische Isotopenmuster (`Isotope Patterns`):**
   - **Kohlenstoff ($^{13}\text{C}$, $1.1\,\%$ pro C-Atom):** $[M+1]^+$-Intensität $\approx 1.1\,\% \times n_\text{C}$ (z. B. bei $20\text{ C}$-Atomen $\sim 22\,\%$ des $M$-Peaks!).
   - **1 Chloratom ($\text{Cl}_1$):** $^{35}\text{Cl} : {}^{37}\text{Cl} \implies \mathbf{M : (M+2) \approx 3 : 1}$ ($100\,\% : 32\,\%$).
   - **2 Chloratome ($\text{Cl}_2$):** $\mathbf{M : (M+2) : (M+4) \approx 9 : 6 : 1}$.
   - **1 Bromatom ($\text{Br}_1$):** $^{79}\text{Br} : {}^{81}\text{Br} \implies \mathbf{M : (M+2) \approx 1 : 1}$ ($100\,\% : 97\,\%$, markanter Doppelbalken!).
   - **2 Bromatome ($\text{Br}_2$):** $\mathbf{M : (M+2) : (M+4) \approx 1 : 2 : 1}$.
   - **1 Cl + 1 Br:** $\mathbf{M : (M+2) : (M+4) \approx 3 : 4 : 1}$.
   - **Schwefel ($^{34}\text{S}$, $4.2\,\%$ pro S-Atom):** Erhöht den $[M+2]$-Peak um $+4.4\,\%$ pro Schwefelatom.
4. **Exakte Masse (`HRMS`):** Für eine Summenformel-Bestätigung ist ein Massen-Fehler **$\Delta m \le \pm 5\text{ ppm}$** bei gleichzeitig geprüftem Isotopenmuster zwingend; bei **ESI-MS** niemals vergessen, dass **Natrium- ($[M+\text{Na}]^+ = M + 22.9892$)** und **Ammonium-Addukte ($[M+\text{NH}_4]^+ = M + 18.0338$)** oft intensiver sind als $[M+\text{H}]^+ = M + 1.0073$!
   - **Kontaminations-Alarm in ESI:** Serien mit **$\Delta m = 44.0262$** ($m/z\ 44, 58, 89 \dots$) = **PEG**; zyklische Siloxane ($m/z\ 371, 445$) = Septum-/Säulenbluten; **$m/z\ 149, 279, 391$** = **Phthalate** (Weichmacher aus Kunststoffspritzen/-schläuchen)!

#### B. Die wichtigsten `EI-MS`-Fragmentierungsmechanismen & Schlüssel-Ionen
- **$\alpha$-Spaltung (`α-Cleavage`, an Ketonen, Ethern, Aminen, Alkoholen):** Radikal am Heteroatom induziert Spaltung der benachbarten $\text{C}_\alpha\text{-C}_\beta$-Bindung unter Verlust des **größten Alkylradikals** zum stabilen Oxonium-/Iminium-/Acylium-Ion ($\text{R-C}\equiv\text{O}^+$)!
  - **Iminium-Serien der Amine (ungerade Elektronen $\rightarrow$ gerade $m/z$!):** $m/z\ \mathbf{30, 44, 58, 72, 86 \dots}$ (`CH2=NH2+` = $30$).
  - **Oxonium-Serien der Alkohole/Ether:** $m/z\ \mathbf{31, 45, 59, 73 \dots}$ (`CH2=OH+` = $31$).
  - **Acylium-Ion bei Benzoesäureestern/Arylketonen:** $m/z\ \mathbf{105}$ ($\text{Ph-C}\equiv\text{O}^+$) $\xrightarrow{-\text{CO}} m/z\ \mathbf{77}$ ($\text{Ph}^+$) $\xrightarrow{-\text{C}_2\text{H}_2} m/z\ \mathbf{51}$.
- **McLafferty-Umlagerung:** Benötigt eine **$\text{C=O}$- (oder $\text{C=N}$-)Gruppe UND ein $\gamma$-ständiges H-Atom**! Über einen 6-Ring-Übergangszustand wird das $\gamma$-H übertragen und ein neutrales **Alken** abgespalten $\rightarrow$ liefert ein **radikalisches Enol-Kation mit GERADZAHLIGEM $m/z$** (z. B. $m/z\ 58$ bei Methylketonen, $m/z\ 74$ bei Methylestern, $m/z\ 88$ bei Ethylestern)!
- **Benzyl-Spaltung $\rightarrow$ Tropylium-Kation ($m/z\ \mathbf{91}$):** Charakteristisch für alle Benzyl-Verbindungen ($\text{Ar-CH}_2\text{-R}$, über Umlagerung zum $6\pi$-aromatischen $\text{C}_7\text{H}_7^+$-Tropylium-Ion; zerfällt weiter unter Verlust von Acetylen $\text{C}_2\text{H}_2$ zu $m/z\ \mathbf{65}$!).
- **Retro-Diels-Alder-Spaltung (`RDA`):** Cyclohexen-Ringe zerfallen im EI-MS durch konzertierte $[4+2]$-Cycloreversion in das konjugierte Dien-Kation + neutrales Dienophil (oder umgekehrt).
- **Neutralverluste (`Neutral Losses`):** $-18$ ($\text{H}_2\text{O}$, Alkohol), $-28$ ($\text{CO}$ oder $\text{C}_2\text{H}_4$), $-32$ ($\text{MeOH}$, Methylester), $-42$ (Keten $\text{CH}_2\text{=C=O}$ aus Acetaten/Acetaniliden!), $-44$ ($\text{CO}_2$), $-60$ ($\text{AcOH}$ aus Acetatestern!).

#### C. `matchms` / `pyOpenMS` & Regulatorische Validierung (`ICH Q2(R2)` / `ICH M10`)
- **`matchms`- & `pyOpenMS`-Regeln:**
  - Cosine-Scores (`CosineGreedy`, `ModifiedCosineGreedy`) nutzen **absolute `Da`-Toleranz**, **nicht `ppm`**; Abfrage- und Referenzspektren stets identisch filtern; bekannte Bugs vermeiden (`FlashSimilarity` mit `spectral_entropy` + `neutral_loss` zählt doppelt!).
  - **`pyOpenMS`:** Nie bereits zentroidierte Daten erneut peak-picken (`isSorted()` bedeutet nicht zentroidiert); keine Normalisierung innerhalb eines Scans (`to_one`) bei label-freier Quantifizierung.
  - **Identifikations-Konfidenz (MSI Level 1 vs. Level 2):** MS¹-Formel oder Bibliotheks-Cosine (NIST $\ge 900$) allein ist nur **putativ**; bestätigte Strukturidentität erfordert **orthogonale Retentionszeit / RI + MS/MS-Abgleich mit authentischem Standard** (bei Stereoisomeren: Co-Injektion!).
- **ICH Q2(R2) (Validierung analytischer Verfahren) & ICH M10 (Bioanalytik):**
  - **$r^2$ beweist KEINE Linearität!** Immer **Lack-of-Fit-Test**, **Residuenplot** und Back-Calculated-Error über mindestens $5$ Konzentrationen auswerten.
  - **DL & QL:** $\text{S/N } 3:1$ ($\text{DL}$) und $\text{S/N } \ge 10:1$ ($\text{QL}$) bzw. $3.3\sigma/S$ und $10\sigma/S$, **plus zwingende experimentelle Bestätigung am Limit** ($\text{QL} \le \text{Reporting Threshold}$); bei $\text{RRF} \notin [0.8, 1.2]$ Response-Faktor-Korrektur anwenden!
  - **LC-MS/MS System Suitability & MRM:** Mindestens **$8\text{--}10$ Datenpunkte pro Peak**, $2$ MRM-Übergänge (`Quantifier` + `Qualifier` mit Ionenverhältnis $\pm 20\text{--}30\,\%$), Carryover nach ULOQ **$< 20\,\%$ LLOQ** (und $\le 5\,\%$ IS), SST-Flächen-RSD $\le 15\,\%$.

<a id="sec-19"></a>
### 4.5 Organometall-, Photoredox- & Elektrochemische Charakterisierung (`organometallic-chemist`, `photochemist`, `electrochemist`)

1. **Organometall-Katalyse & Homogenitäts-Kontrolle (`organometallic-chemist`):**
   - **Elektronenzählung (`CBC-Methode`, Green):** $\text{L}$-Liganden ($2e^-$-Donoren: $\text{PR}_3, \text{CO}, \text{Alkene}, \text{THF}$) vs. $\text{X}$-Liganden ($1e^-$-Radikal / anionisch: $-\text{H}, -\text{R}, -\text{Ar}, -\text{Cl}, -\text{OAc}$); $\eta^n$-Koordination (Allyl $= \text{LX}$, Cyclopentadienyl $= \text{L}_2\text{X}$). Koordinativ ungesättigte $14e^-$/$16e^-$-Komplexe ermöglichen Oxidative Addition und Insertion.
   - **Elementarschritte & Diagnostik:** `OA` (erfordert elektronenreiches $\text{M}^n$), `RE` (beschleunigt durch großen Bite-Angle und sterischen Druck), Migratorische Insertion (streng *syn*!), $\beta$-Hydrid-Eliminierung (erfordert leeres *cis*-Koordinationsorbital und *syn*-coplanares $\beta$-H), Transmetallierung.
   - **Katalyse-Artefakt-Tests (`Base-Metal` vs. `Trace-Pd` vs. Nanopartikel):** Aktivität durch **ppb-Spuren von Palladium** in vermeintlich „metallfreien“ oder Eisen-/Kupfer-/Nickel-katalysierten Reaktionen ausschließen; bei Verdacht auf kolloidale Nanopartikel (`Grubbs-Ru`, $\text{Pd}^0$-Kolloide) **Heißfiltration (`Hot Filtration`)**, **$\text{Hg(0)}$-Vergiftungstest**, **$\text{PPh}_3$/$\text{CS}_2$-Vergiftungsstudien**, **TEM** und **ICP-MS** durchführen!
   - **Leistungskennzahlen:** Immer **Turnover Number (`TON`)** $= \frac{n_{\text{Produkt}}}{n_{\text{Katalysator}}}$ und **Turnover Frequency (`TOF`)** $= \frac{\text{TON}}{t}$ samt Substrat/Katalysator-Verhältnis (`S/C`) und Temperatur berichten.
2. **Photochemie & Photoredox-Katalyse (`photochemist`):**
   - **Jablonski-Diagramm & Stern-Volmer-Löschung:** Quantenausbeute $\Phi = \frac{n_{\text{Reaktion}}}{\text{absorbierte Photonen [Einstein]}}$ (Kettenprozesse geben $\Phi > 1$!); Lebensdauer $\tau = \frac{\Phi_f}{k_f + k_{nr}}$; dynamische vs. statische Löschung über $\frac{F_0}{F} = 1 + K_{\text{SV}}[Q]$ plus Lebensdauermessung ($\tau_0/\tau$) unterscheiden; Aktinometrie mit **Kaliumferrioxalat**.
   - **Praxis-Fallstricke:** Gelöster **Triplett-Sauerstoff ($\text{O}_2$)** löscht angeregte Triplett-Zustände ($T_1$) diffusionskontrolliert und bildet Singulett-Sauerstoff ($^1\text{O}_2$) $\rightarrow$ vor Photoredox-Reaktionen zwingend per **`Freeze-Pump-Thaw`** entgasen! Zudem **Inner-Filter-Effekt** und Photodegradation des Substrats von echter Photokatalyse abgrenzen (Dunkelkontrolle + Kontrolle ohne Photokatalysator!).
3. **Organische Elektrochemie (`electrochemist`, Kolbe / Shono / e-Reduktion):**
   - **Thermodynamik vs. Kinetik:** Nernst-Gleichung bestimmt Gleichgewichtspotential $E_{\text{eq}} = E^\circ - \frac{RT}{zF}\ln\left(\frac{a_{\text{red}}}{a_{\text{ox}}}\right)$; Überspannung $\eta = E - E_{\text{eq}} = \eta_{\text{act}} + \eta_{\text{conc}} + i R_u$.
   - **Praxis-Fallstricke bei CV & präparativer Elektrolyse:** Unkompensierten Lösungswiderstand (**$iR_u$-Drop**) bei nicht-wässrigen Elektrolyten ($\text{MeCN}/\text{Bu}_4\text{NPF}_6$) korrigieren; Referenzpotential immer gegen **Ferrocen ($\text{Fc/Fc}^+$)** kalibrieren; **Faradaysche Effizienz (`FE`)** berechnen und **geteilte vs. ungeteilte Zelle** wählen (wenn das Produkt an der Gegenelektrode re-oxidiert/-reduziert wird, zwingend geteilte Zelle oder Opferanode nutzen!).
