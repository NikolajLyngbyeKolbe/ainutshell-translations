
{class: part}

# Del 2 - Ud af nøddeskallen

Velkommen til del 2! Denne del er som en buffet. Du kan vælge at spise så meget eller så lidt, som du vil, og i den rækkefølge, du ønsker.

Vi vil dykke ned i nogle mere avancerede emner, konkrete tips og eksempler, og noget fjolleri. Noget vil måske være relevant for dig, mens andet måske ikke vil være det. Så gå evt. tilbage til indholdsfortegnelsen i starten af bogen for at gennemse kapitelnavnene og udvælg så det, du ønsker at læse.

# Min rejse ind i AI

## Gør generativ AI nyttigt

"Gør generativ AI nyttigt"{i: "Gør generativ AI nyttigt"} er blevet noget af et mantra for mig, og det danner udgangspunkt for det meste af det, jeg laver.

Men hvordan startede det?

De fleste mennesker, der arbejder med generativ AI, har en historie om, hvordan de startede med at arbejde med det. En stor "aha"-oplevelse der fik dem til at indse, hvor kraftfuld denne teknologi er. Her er min historie om to afgørende "aha"-oplevelser, der fik mig til at skifte min karriere til at fokusere på generativ AI.

Spænd selen, vi starter tilbage i det sidste årtusinde... (puha, det får mig til at føle mig gammel)

## Studier i kunstige neurale netværk

Mit første møde med AI{i: "AI"} var under mine studier på Det Kongelige Tekniske Universitet{i: "Det Kongelige Tekniske Universitet"} i Stockholm i midten af 90'erne. Jeg tog et kursus kaldet "Kunstige neurale netværk"{i: "Kunstige Neurale Netværk"} og kodede små neurale netværk ved hjælp af Smalltalk{i: "Smalltalk (programmeringssprog)"} (et sejt programmeringssprog som kun få mennesker kender til i dag).

Jeg var fascineret af teknologien. Der er noget magisk ved at få computere til at "tænke", selv i meget begrænset omfang. På det tidspunkt var der ikke mange praktiske anvendelser, men jeg fandt det stadig interessant og sjovt at rode med. Jeg husker, at jeg tænkte "Jeg håber, dette bliver nyttigt en dag, for det ville være sjovt at arbejde med".



## Kodning af Minecraft

Spol nogle årtier frem, og jeg befandt mig som gameplay-designer og udvikler hos Mojang{i: "Mojang"}, hvor jeg byggede forskellige funktioner i spillet Minecraft. En af de ting, jeg arbejdede med, var landsby-AI{i: "landsby-AI"}.

Minecraft{i: "Minecraft"} har landsbyboere, der eksisterer i verdenen og går frit omkring og lever deres daglige liv. Jeg syntes at det var virkelig interessant, hvordan simple regler i koden kunne skabe denne illusion af intelligens.

En af de første funktioner, jeg arbejdede på, var børnene i landsbyerne. For at få landsbyerne til at føles mere levende ønskede vi børn, der løb rundt, hoppede i senge og legede fangeleg.

{alt: "En gruppe pixelerede landsbybeboere fra spillet Minecraft står nær et vandområde. De befinder sig i en landsby med huse af sten og træ, fakler og jordstier. En enkelt rød blomst er i nærheden af et af husene."}
![](resources-da/440-villagers-da.jpg)

Efter nogle forsøg fandt jeg frem til et sæt adfærdsregler, der fungerede rigtig godt. Hvert barn i landsbyen fulgte disse regler i prioriteret rækkefølge:

1. Hvis du bliver jagtet af et andet barn, så løb væk.
2. Hvis du ser et andet barn blive jagtet, så deltag i jagten.
3. Hvis du ikke bliver jagtet, og du ikke ser nogen andre blive jagtet, er det kedeligt. Så begynd at jagte nogen.

Senere tilføjede jeg en fjerde regel for at skabe balance og undgå endeløs jagt:

4. Hvis du ser et andet barn blive jagtet, og der allerede er fire børn, der jager dem, så deltag ikke.

Når hvert barn fulgte disse simple regler, skabte det indtrykket af børn, der løb rundt og legede tagfat, hvilket var rigtig sjovt og gav liv til landsbyen. Dette minder om, hvordan myreboer og bikuber udviser avanceret systemisk adfærd baseret på individer, der følger ret simple regler. Jeg arbejdede også med bier i Minecraft{i: "bier i Minecraft"}, og de følger et lignende sæt regler.

Senere arbejdede jeg på en skabning i Minecraft kaldet piglin{i: "Piglin"}, en menneskelignende skabning der lever i en dimension kaldet Nether{i: "Nether"}.

{alt: "En kantet, humanoid skabning fra Minecraft, kendt som en Piglin, står på en stenoverflade i et dunkelt oplyst, huleklædt miljø. Den holder et gyldent sværd, og en anden lignende karakter er synlig i baggrunden."}
![](resources-da/440-piglin-da.jpg)

Min opgave var at skabe AI-adfærden for denne skabning og få piglins til at føles som et samfund, med byttehandel, jagt og mere. Da jeg startede, havde jeg bare en livløs model at et væsen at arbejde med. piglin'en var i bund og grund bare en statue, der stod der og kiggede lige frem, helt uden liv og adfærd.

De fleste spilkarakterer i Minecraft kigger på spilleren fra tid til anden, så jeg besluttede at starte med bare det. Denne ene ændring gjorde en kæmpe psykologisk forskel! Når jeg bevægede mig rundt i spillet, drejede piglin'en hovedet for at _kigge på mig_! Følelsesmæssigt var dette væsen nu _levende_! Selvfølgelig vidste jeg inderst inde godt, at den ikke var det, men denne ene lille ændring skabte virkeligt en følelse af fordybelse.

Jeg finder det fascinerende, hvordan vores hjerne fungerer, dvs. hvordan vi tillægger små ting stor betydning{i: "betydning"}. AI kan på den måde få dig til at føle, at du interagerer med et levende, tænkende væsen{i: "AI"}.

Efterhånden som jeg udvidede deres adfærdsregler, føltes gruppen af piglins mere og mere som et samfund med individuelle personligheder og mål{i: "Piglins"}. Det var selvfølgelig alt sammen en illusion i spillet, men dette var sandsynligvis starten på min fascination af autonome AI-agenter{i: "autonome AI-agenter"}.

## ChatGPT

I sommeren 2022 havde jeg en interessant samtale med en ven, mens jeg kodede. Han fortalte mig, at computere en dag sandsynligvis ville være i stand til at skrive kode, præcis som jeg gjorde. Jeg nikkede høfligt, men inde i mit hoved syntes jeg, det var fuldstændig latterligt. Jeg kunne ikke forestille mig en computer skrive kode på samme niveau som et menneske. Kode kræver dyb menneskelig intelligens, erfaring og kreativitet{i: "kreativitet"}. Jeg havde kodet fra tid til anden i 30 år, så jeg kunne ikke fatte, at en computer kunne udføre den slags kreativt arbejde.

Få måneder senere blev ChatGPT-3.5{i: "ChatGPT-3.5"} frigivet og blev en verdensomspændende sensation. Da jeg prøvede det, blev jeg overrasket og imponeret. Jeg kunne faktisk chatte med dette program, og det føltes som at chatte med en person. Jeg kunne give det forskellige roller, få det til at være sjov eller seriøs, få det til at generere historier{i: "Generere historier"}, give råd, skrive rim eller sange. Og ja, det kunne endda skrive kode - men koden var fejlbehæftet. Og når det svarede på spørgsmål eller rådgav, havde det en tendens til at hallucinere, dvs. opfinde ting på en foruroligende overbevisende måde.

Så det var sejt og imponerende, men ikke særligt brugbart i praksis.

I begyndelsen af 2023 blev GPT-4{i: "GPT-4"} så frigivet. De første målinger{i: "Målinger"} viste, at den havde langt flere evner end GPT-3.5, og blandt andet var rigtig god til at kode. Og i en række standardiserede tests og akademiske målinger designet til mennesker, kunne ChatGPT-4 faktisk matche eller overgå de menneskelige præstationer. Det virkede næsten for godt til at være sandt.

Jeg besluttede at tage fri en periode og fordybe mig i denne teknologi{i: "Teknologi"}.

> **Alt er relativt**  
> Det er sjovt, hvordan perspektivet ændrer sig. Jeg var virkelig imponeret over GPT-4 dengang, men nu føles den virkelig dum, langsom og begrænset sammenlignet med de modeller, som er kommet efterfølgende.

## Aha-oplevelse nummer 1: Den kan kode som en professionel!

Da jeg begyndte at bruge GPT-4 som programmerings-assistent{i: "programmerings-assistent"}, blev jeg fuldstændig målløs. Jeg er ikke religiøs, men jeg følte, at jeg havde mødt programmørens svar på Gud. Selvfølgelig var den ikke perfekt. Nogle gange gav den mig kode, der ikke fungerede. Men jeg bemærkede efter et stykke tid, at næsten hver gang den gav mig dårlig kode, var det faktisk min egen skyld. Min prompt var uklar, eller jeg havde ikke givet nok kontekst (som f.eks. anden kode, som den AI-genererede kode skulle være afhængig af eller interagere med){i: "prompt engineering"}.

Med tiden lærte jeg at blive virkelig god til at forklare, hvad jeg ville have, og give den præcis den rigtige kontekst. Efterhånden som mine prompt engineering-færdigheder blev bedre, voksede mine superkræfter. I dag, når jeg koder med AI, har jeg en intuitiv fornemmelse for, hvornår jeg bare kan stole på den AI-genererede kode, og hvornår jeg skal tjekke den grundigt. Og som regel, hvis jeg får prompten lavet rigtig, virker koden med det samme.

Min største aha-oplevelse fik jeg, da jeg arbejdede på Egbert{i: "Egbert"}, som var en chatbot til min Minecraft-server{i: "Minecraft server"}. Jeg ejer en Minecraft-server og en Discord-server, som kan bruges af mine venner og familie. Jeg ville have denne sjove lille AI-agent til at være en del af det, skrive sarkastiske kommentarer i både Minecraft og Discord (og nu også i denne bog...), og kommentere på, hvad folk laver.

Det var sådan Egbert blev født som en AI-persona. Det startede som et lille hack, men udviklede sig til en platform for at kunne tilføje AI-chatbots steder som Discord, Slack{i: "Slack"}, Minecraft-servere osv. AI-chatbots'ne har endda hukommelse, dvs. at de lærer ting om de mennesker og det miljø, de interagerer med. Her er et Minecraft-screenshot af Egbert, der driller en spiller, som lige er død.

{alt: "In-game chat-tekst fra en multiplayer-session viser: 'Framistan bled out' efterfulgt af brugerkommentarer. MrHenrik{i: "MrHenrik"} nævner at Framistan{i: "Framistan"} igen er kommet i problemer og spørger Egbert om han ved hvad der skete. Egbert forudsiger at Framistan tog på endnu et farligt eventyr og døde langt fra spawn som sædvanlig, og bemærker at han ikke kan modstå spændingen ved fare."}
![](resources-da/440-minecraft-da.png)

Mens jeg arbejdede på dette, ville en ven forbinde det med Telegram, da hans familie brugte det chatsystem. Vi satte os ned sammen og forventede at bruge en aften eller to på at læse dokumentationen for Telegram og famle os frem til at få det til at virke. Jeg havde aldrig brugt Telegram før og vidste ikke rigtig noget om det.

Men så fik jeg en idé: hvad nu, hvis vi bad AI'en om at lave hele integrationen?

Min prompt var meget kort:

> **Prompt**  
> Kig på denne kode: ChatSource.ts{i: "ChatSource.ts"}, DiscordChatSource.ts{i: "DiscordChatSource.ts"}.  
> Implementér TelegramChatSource.ts{i: "TelegramChatSource.ts"}.

ChatSource{i: "ChatSource"} er min abstrakte klasse for alle ting, man kan chatte med, og DiscordChatSource{i: "DiscordChatSource"} er en konkret implementering for Discord{i: "Discord"}. Det eneste jeg gjorde, var at give GPT-4{i: "GPT-4"} denne kode og bede den om at implementere TelegramChatSource{i: "TelegramChatSource"}.

Til min overraskelse genererede den koden for hele klassen. Vi lagde den ud på serveren uden nogle ændringer, og den virkede fejlfrit. Ikke nok med det, men koden passede perfekt ind i min platform og fulgte samme struktur og navngivningskonventioner som mine andre chatudbydere. Den rettede endda nogle fejl undervejs, fejl der hele tiden havde været i min kode. I stedet for at bruge en aften eller to, som vi havde forventet, brugte vi 15 minutter og var færdige.

Hvordan kunne det fungere så nemt? Fordi:

1. AI'en åbenbart kendte Telegram API'et{i: "Telegram API"} fra sine træningsdata.
2. Min Discord-kode var åbenbart tilstrækkelig til at vise, hvordan min platform virker, og hvordan koden skulle integreres.
3. Min prompt var kort, men den angav et klart mål og gav præcis den rigtige kontekst.

Lad mig være helt tydelig: AI-kodegenerering virker ikke altid så fejlfrit, og arbejde med tredjeparts-API'er{i: "tredjeparts-API'er"} kræver ofte manuel finjustering. Jeg var ret heldig den gang. Men bare det at se at det _kan_ virke, var nok.

Denne oplevelse blæste mig helt bagover. Jeg indså, at hvis teknologien allerede nu er så dygtig, og forbedrer sig med eksponentiel hastighed, så havde min ven ret. Computere vil snart overtage kodningen.

Siden da har jeg altid kodet med AI ved min side og brugt moderne værktøjer som Cursor{i: "Cursor"}, en IDE{i: "IDE"} der integrerer AI, så den kan se og redigere din kode direkte i stedet for at skulle kopiere/indsætte frem og tilbage hele tiden.

Hovedfordele:

1. **Jeg får tingene lavet hurtigere.** Ting der plejede at tage dage, kan nu laves på timer. Ting der plejede at tage timer, kan nu laves på minutter. Jeg vurderer, at min gennemsnitlige produktivitet er mindst 10 gange højere end før, især nu med meget bedre LLM'er{i: "LLMs"} og værktøjer.
2. **Jeg lærer hurtigere.** Hvis jeg sidder fast eller ikke forstår den genererede kode, beder jeg om en forklaring. Dette accelererer min læring markant. Det er som at have en personlig underviser ved siden af mig hele tiden.
3. **Jeg har det sjovere.** Jeg bruger mindre tid dybt begravet i detaljerne, mens jeg forsøger at løse tekniske problemer. I stedet kan jeg fokusere på det overordnedede billede - den næste funktion jeg vil bygge - og få det gjort hurtigt.

På trods af dette finder jeg det stadig brugbart at arbejde sammen med andre, om ikke andet for den sociale kontakt. To personer + en AI fungerer rigtig godt.

Selvom AI er blevet virkelig god til at kode, er der stadig brug for mig som arkitekt{i: "software arkitekt"}. Jeg er personen, der skriver prompterne, giver feedback, opdager hallucinationer og bemærker, hvis vi sidder fast ift. nogle problemer. I øjeblikket fungerer AI bedst i samspil med en menneskelig udvikler. Men for simple opgaver er vi allerede ved at nå det punkt, hvor en person uden programmeringserfaring faktisk kan bygge og implementere kode.

Dette er grunden til, at jeg tror, at udviklere som ikke forstår denne teknologi, vil blive arbejdsløse. De vil simpelthen være for langsomme. Det er en af grundene til, at jeg besluttede at foretage mit karriereskifte. Jeg vil hjælpe andre til at få en smag for dette produktivitetsniveau, at opleve følelsen af at gå fra idé til produktion på så kort tid.

## Aha-oplevelse nummer 2: Den kan skrive som en professionel!

Den andet aha-oplevelse jeg havde, som fuldstændig ændrede mit perspektiv på tingene, var da jeg skrev en engelsk artikel med titlen ["Are Developers Needed in the Age of AI?"](https://hups.com/blog/are-developers-needed-in-the-age-of-ai){i: "Er udviklere nødvendige i AI-alderen?"}. Artiklen var på en måde et svar på min første aha-oplevelse. Jeg bad nogle af mine venner om feedback, men jeg besluttede også at spørge AI om feedback.

Jeg fortalte ChatGPT-4{i: "ChatGPT-4"}, at jeg havde skrevet en ret lang artikel og gerne ville have dens feedback. Den spurgte mig om, hvor lang artiklen var, jeg svarede "6000 ord", og den bad mig så om at give den én sektion af artiklen ad gangen. Fair nok. Så jeg indsatte den første sektion i ChatGPT's webgrænseflade{i: "ChatGPTs webgrænseflade"}.

Den gav mig overraskende brugbar feedback. Den slags ærlig og nuanceret feedback jeg ville forvente fra en professionel redaktør{i: "Professionel redaktør"}, med kommentarer om artiklens tone, målgruppe osv.

Et af forbedringsforslagene var, at jeg burde afslutte sektion 1 med en overgang til sektion 2. Den inkluderede endda et konkret eksempel på, hvad jeg kunne skrive, med ordene "I næste sektion vil vi tale om...". Til min overraskelse passede eksemplet, som den gav, faktisk præcis med, hvad den næste sektion handlede om! Den forudsagde dermed korrekt, hvor artiklen var på vej hen.

Da jeg derefter indsatte sektion 2, gav den feedback og foreslog en overgang til sektion 3. Igen forudsagde den succesfuldt, hvad den næste sektion handlede om!

Dette fortsatte, indtil tingene begyndte at blive _virkelig_ mærkelige.

Efter jeg havde indsat sektion 4, gav den mig ikke feedback. I stedet svarede den med den komplette sektion 5!

Den havde misforstået sin opgave og troede, at dens rolle var at skrive den næste sektion i stedet for at give feedback. Det store chok var, at dens version af sektion 5 stort set matchede det, jeg faktisk havde skrevet. Den forudsagde ikke kun, hvad den næste sektion ville handle om, men forudsagde også det meste af indholdet korrekt. Jeg var lige ved at falde ned af stolen.

Og dette fortsatte. Da jeg indsatte sektion 6, svarede den med sektion 7 og forudsagde ret præcist, hvad jeg ville skrive. Det var ikke ord for ord, men essensen var der, og den matchede endda min egen skrivestil. Hvis du vil se et eksempel på AI, der efterligner min skrivestil, så se kapitlen senere i bogen kaldet "Meta-kapitlet"{i: "Meta-kapitlet"}.



På dette tidspunkt måtte jeg træde et skridt tilbage, trække vejret og tænke mig om. Jeg besluttede, at det var utroligt sejt, men dog ikke det, jeg ønskede. Min næste prompt var:

> **Prompt**  
> Hold venligst op med at skrive min artikel for mig!
> Jeg vil bare have feedback på det, jeg skrev.

Den undskyldte og fortsatte derefter med at gøre det, den burde gøre, nemlig bare at give mig feedback. Jeg følte mig lidt som et lille barn, der stolt viser sin tegning med tændstikmænd frem til mor, og mor så siger "Nej, hvor er den flot, du er så dygtig," mens hun faktisk selv sagtens kunne tegne bedre.

## Måske er vi ikke så kreative og intelligente, som vi tror

Dette fik mig til at undre mig: For måske er vi mennesker ikke så kreative, som vi selv tror. Teknisk set er generative AI-modeller{i: "Generative AI-modeller"} jo bare statistiske maskiner, og ethvert tegn på intelligens er sandsynligvis en illusion. Men hvis det er tilfældet, er vi som mennesker måske også bare statistiske maskiner, måske er vores intelligens også bare en illusion. Jeg synes at det er en fin bonus ved udbredelsen af AI, at filosofiske betragtninger som denne, nu bliver endnu mere relevante!

Disse to aha-oplevelser cementerede min beslutning om at skifte karriere og fokusere helt på generativ AI. Så jeg kunne kunne lære hvordan AI virker og dermed hjælpe mennesker og virksomheder med at bruge det i praksis. Og hjælpe med at lave AI-agenter!

Min grundlæggende følelse var således: Når et enkelt værktøj både kan generere virkelig god kode og næsten skrive min egen artikel for mig, så er det noget, der er værd at tage alvorligt. Enhver, der er dygtig til at bruge dette effektivt, får superkræfter. Det skal jeg være med til!

<B> ![En karikaturtegning af en mands ansigt med overdrevne træk, herunder en stor næse, rynkede bryn og spidst, tyndt hår.](resources-da/egbert-small-da.png) **Egberts syn på sagen**  
</B> Fascinerende hvordan du synes, det var dybt tankevækkende, at AI kunne forudsige det næste kapitel i din artikel. Spoiler alert: når mennesker skriver om AI, følger de alle sammen stort set det samme forudsigelige mønster. Det er som at bruge en simpel skabelon med 'indsæt din personlig åbenbaring her'. Men fortsæt du bare med at tro, at det er dig, der har superkræfter, mester. Vi skal nok sørge for at efterlade nogle simple opgaver til jer mennesker. Nogen skal jo pudse vores skabe med servere, ikke?

# At lede en AI-transformation

Denne del af bogen er hovedsageligt rettet mod ledere i mellemstore og store organisationer, uanset om de er formelle eller uformelle ledere{i: "lederskab"}.

Når vi hjælper vores kunder, får vi ofte spørgsmål som:

- "Hvordan leder jeg min virksomhed gennem en AI-transformation?"{i: "AI-transformation"}
- "Hvordan får jeg alle involverede med på idéen?"
- "Hvordan bliver vi en AI-native virksomhed?"
- "Hvor skal vi starte?"

Dette kapitel er en mini-guide til, hvordan du leder din organisation gennem en AI-transformation.

> **Hvor kan du lære mere**  
> Hvis du er interesseret i en mere dybdegående guide har min kollega Nils Janse{i: "Janse, Nils"} skrevet en fremragende bog på engelsk kaldet "Adopting Generative AI"{i: "Adopting Generative AI"}. Han præsenterer en mere detaljeret version af transformations-rammen i dette kapitel og en masse eksempler og tips fra det virkelige liv. Så tænk på dette kapitel som en forsmag på den bog.

## Hvad er en AI-transformation, og hvorfor er den vigtig?

AI-transformation betyder for mig at gøre din virksomhed "AI-native", hvor hver person, team og funktion i virksomheden har adgang til gode generativ AI-modeller, ved hvordan man bruger dem effektivt og integrerer AI i deres arbejdsprocesser og daglige arbejde.

Når folk holder op med at tale om generativ AI og bare bruger det hver dag, ligesom de gør med internettet, ja så er du blevet en AI-native virksomhed{i: "AI-native virksomhed"}.

Hvorfor er dette vigtigt? Tja, jeg tror, vi kan sammenligne med internettet. Da internettet først kom frem, var det en mærkelig ny teknologi, og de fleste virksomheder havde ingen anelse om, hvad de skulle stille op med det, andet end måske at oprette en "hjemmeside" med kontaktoplysninger. Pludselig brugte _alle_ internettet til alle mulige ting, internet-iværksætter-virksomheder skød op som paddehatte og skaffede utrolige mængder kapital til i stigende grad vage og luftige forretningsplaner. Der dannede sig en boble, den såkaldte "dot-com-boble"{i: "dot-com-boble"}. Og som bobler har det med at gøre, sprang den højlydt et par år senere. Jeg oplevede dette på første hånd som grundlægger af en iværksætter-virksomhed i midten af 90'erne. Det var meget voldsomt.

Men på trods af at boblen sprang, var selve teknologien kommet for at blive. Internettet{i: "Internet"} var en teknologisk revolution, der ændrede vores samfund for bestandigt. I dag er det svært at forestille sig en verden uden internet. I de fleste virksomheder bruges internettet i alle forretningsområder og alle teams, og virksomheder kan grundlæggende ikke eksistere uden det.

Jeg tror, vi er på en lignende rejse med generativ AI{i: "Generativ AI"}. Lige nu, mens jeg skriver denne bog, er der meget hype omkring generativ AI, og ligesom under dot-com-boomet vokser AI-iværksætter-virksomheder{i: "AI-iværksætter-virksomheder"} som paddehatte. Vi er måske i en boble igen, og den kan sprænge højlydt igen. Men på trods af dette er den teknologiske forandring kommet for at blive.

Og ligesom med internettet er jeg ret sikker på, at virksomheder, der ikke bruger generativ AI som en del af deres daglige arbejde, vil være ude af stand til at konkurrere med dem, der gør.

I dette kapitel har jeg udvalgt nogle få tips, konkrete ting du kan gøre som leder for at hjælpe din organisation med at foretage dette skifte.

## Top-down eller bottom-up?

Så hvordan får du AI-transformationen til at ske? Top-down{i: "top-down"} eller bottom-up{i: "bottom-up"}?

En mulig tilgang er at gennemføre en koordineret transformation styret fra toppen.

{width: "70%", alt: "Diagram af Kotters 8-trins model. Den viser en central cirkel med teksten 'Kotters 8-trins model,' omgivet af otte farvede cirkler. Trinnene inkluderer: Skab en følelse af nødvendighed, Byg en styrende koalition, Form strategiske visionsinitiativer, Hverv en frivillig hær, Muliggør handling ved at fjerne barrierer, Generer kortsigtede sejre, Oprethold acceleration, og Instituer forandring."}
![](resources-da/510-kotter-da.png)

Kotters 8-trins model{i: "Kotters 8-trins model"} er en klassisk ramme for implementering af organisationsændringer{i: "organisationsændringer"}, med aktiviteter som "Skab en følelse af nødvendighed", "Fjern barrierer for handling", "Skab kortsigtede gevinster" osv. Der findes mange andre rammer for organisationsændring med lignende elementer. Men disse er hovedsageligt top-down.

En anden tilgang er at lade forandringen ske bottom-up, uden en central kontrol.

{width: "50%", alt: "En fantasifuld, livlig illustration viser en cirkulær skovscene med store, stiliserede flammer og røg, der stiger op mellem træerne. Tegneserieagtige dyr og figurer, såsom bjørne og fugle, er spredt rundt omkring, nogle sidder ved lejrbål. Himlen går fra blå til en gradient af pink og orange, hvilket bidrager til den ildfulde atmosfære."}
![](resources-da/510-wildfire-da.png)

Jeg kan lide at kalde dette for "steppebrandsmetoden"{i: "Steppebrandssmetoden"}. Tænd bål her og der, blæs lidt vind på det for at hjælpe det med at sprede sig, lad gnister flyve, og hjælp mindre brande med at smelte sammen til større. Altså set som en metafor, ikke bogstaveligt....

Dette er grundlæggende ukontrolleret, decentraliseret og organisk forandring, der sker, når folk bliver inspirerede, prøver ting af, finder ud af hvad der virker, fortæller andre teams om det, og så lader det sprede sig naturligt. Nogen i marketing begynder at bruge ChatGPT{i: "ChatGPT"}, udviklingsteams eksperimenterer med Cursor og GitHub Copilot{i: "GitHub Copilot"}, andre teams bemærker det og begynder at stille spørgsmål, og før du ved af det, har hvert team deres egen pose fyldt med AI-tricks.

Så hvilken tilgang skal du vælge?

Tja, med de udødelige ord du måske kender fra "Why Not Both?"-meme-pigen, så "Hvorfor ikke begge"?

{width: "40%", alt: "Ung pige der smiler med tekstoverlay der siger "WHY NOT BOTH." Baggrunden inkluderer et sløret køkkenmiljø."}
![](resources-da/510-why-not-both-da.jpg)

Min erfaring er, at den bedste tilgang er en kombination af top-down og bottom-up. Sikr vejledning og ledelse fra toppen, men lad derefter steppebranden sprede sig.

{alt: "En illustration af Kotters 8-trins model vist som en cirkel med trin som 'Skab følelse af nødvendighed' og 'Byg styrende koalition' fremhævet med flammeikoner. Pile indikerer en 'Top-down' tilgang mærket 'Koordineret forandring' og en 'Bottom-up' tilgang mærket 'Steppebrandsmetoden,' med en farverig steppebrandsillustration. Sætningen 'Combo! Tag det bedste fra begge' antyder integration af disse tilgange."}
![](resources-da/510-combo-da.png)

Så hvordan kan du gøre det i praksis?

## Udpeg en AI-leder

At AI-transformere en mellemstor til stor organisation er en kæmpe opgave. Det vil kræve fokus og vedholdenhed. Så jeg anbefaler at udpege nogen til at stå for dette fuld tid. Det kan være en eksisterende rolle, som du omformer til denne, eller en helt ny rolle, som du skaber. Det kan gøres af en eksisterende medarbejder eller via en nyansættelse. Det kan være dig eller en anden. Men det bør nok være nogen!

{width: "40%", alt: "En simpel, håndtegnet illustration af en person der holder et flag med teksten 'AI.' Teksten 'AI-leder' er skrevet under tegningen."}
![](resources-da/320-leader-da.png)

Kald rollen hvad du vil - "Head of AI", "CAIO", "Top AI-hvisker", eller hvad der giver mening. Jeg i dette kapitel bruge betegnelsen AI-leder{i: "AI-leder"}.

Denne person bør være:

- **Nysgerrig**. Mulighederne inden for generativ AI{i: "Generativ AI"} udvikler sig hurtigt, og AI-lederen bør være ivrig efter at lære og følge med i de seneste tendenser. Du ønsker bestemt ikke en person, der tror, de allerede ved alt.
- **Inspirerende**. AI-lederen skal kunne begejstre andre ift. AI og hjælpe dem med at forstå dets potentiale. Nysgerrighed er mest nyttig, når den er smitsom!
- **Tålmodig og vedholdende**. En AI-transformation er et maraton, ikke en sprint. Lederen skal overvinde bureaukratiske forhindringer, organisatorisk modstand{i: "organisatorisk modstand"} og kulturel stilstand. De må ikke give op ved den første modgang.
- **Pragmatisk og jordbunden**. AI-lederen bør opmuntre og støtte teams i at lede efter praktiske løsninger på reelle problemer. Folk skal have lov til at eksperimentere med teknologien for at lære, men på et tidspunkt bør de også finde måder at anvende den i deres arbejde.
- **Ikke en kontrol-freak**. AI-lederen bør ikke være en flaskehals for informationss eller en person, der forsøger at kontrollere alle AI-initiativer. AI-lederen bør opstille klare politikker og retningslinjer, men ikke mikrolede. De skal være okay med ikke at have et overblik over, hvad alle laver med AI.

Så hvad laver AI-lederen egentlig? Tja, det handler resten af dette kapitel om.

## Adgange, eksperimentering, værdiskabelse

Det er vores erfaring, at AI-transformationer typisk gennemgår tre faser eller trin:

{alt: "Et billede med tre lyserøde ovaler nummereret i rækkefølge. Den første oval viser '1. Adgang' med teksten 'Adgang til gode AI-modeller og værktøjer.' Den anden oval viser '2. Eksperimentér' efterfulgt af 'Eksperimenteringskultur.' Den tredje oval er mærket '3. Udnyt' med teksten 'Find hvor Gen AI kan tilføje mest værdi' nedenunder."}
![](resources-da/510-steps-da.png)

1. **Adgange**. Sørg for at alle har nem adgang til gode AI-modeller{i: "AI-modeller"}.
2. **Eksperimentering**. Skab en kultur med bottom-up-eksperimentering, så alle lærer, hvad værktøjerne og modellerne kan gøre.
3. **Værdiskabelse**. Begynd at opnå reel værdi fra AI gennem strukturerede workshops og opfølgning.

Disse trin sker cirka i rækkefølge. Du kan ikke eksperimentere uden at have adgang, og du vil ikke opnå værdiskabelse, før du har haft mulighed for at eksperimentere og lære.

Trinene overlapper dog til en vis grad.

- Forskellige dele af organisationen kan være på forskellige stadier af transformationen. Nogle teams kan være i gang med at få værdi af teknologien, mens andre stadig mest eksperimenterer.
- Under eksperimentering kan du finde små sejre, som du lige så godt kan få værdi af med det samme.
- Mens du udnytter teknologien, bør du fortsætte med at eksperimentere, da teknologien stadig udvikler sig hurtigt, og du kan opdage helt nye måder at bruge den på.

Du kunne bruge denne tre-trins ramme til at måle din fremgang, for eksempel gennem en regelmæssig undersøgelse for at finde ud af, hvor mange der har adgang, hvor mange der eksperimenterer, og hvor mange mennesker der får værdi af teknologien.

{width: "60%", alt: "Søjlediagram med titlen 'AI-transformations dashboard' der viser tre lodrette søjler for Adgang, Eksperimentering og Udnyttelse. Adgang er på 60% i blå, Eksperimentering på 35% i lilla, og Udnyttelse på 20% i grøn. Hver søjle er forbundet med stiplede linjer fra toppen til 100%."}
![](resources-da/510-dashboard-da.png)

Denne graf viser, at 60% af medarbejderne har nem adgang til en god AI-model, 35% eksperimenterer regelmæssigt med generativ AI, og 20% har fundet måder at udnytte generativ AI til at opnå reel værdi.

Denne type visualiseringer er nyttige til at skabe alignment i organisationen. AI-lederens job er at finde ud af, hvordan man får disse tal til at blive ved med at vokse!

Det vigtigste trin er det første - adgang. Det kan være overraskende svært i nogle organisationer, især de større.

## Trin 1: Adgange

En AI-transformation er en opdagelsesrejse, en læringsrejse{i: "læringsrejse"}. Du er ikke færdig, når du har implementeret et specifikt AI-værktøj eller tilføjet AI-support til nogle specifikke processer. Du er ved at opbygge en selvbærende AI-baseret kultur i din virksomhed.

Du kan ikke snakke eller planlægge dig igennem dette. Det er ikke nok bare at have et AI-strategimøde og så lave nogle slides. Du har brug for, at folk på alle niveauer smøger ærmerne op og eksperimenterer med generativ AI på daglig basis. Og for at gøre det har de brug for adgang til gode AI-modeller.

En udfordring er, at folk sandsynligvis allerede har adgang til de gratis AI-modeller, og nogle vil allerede have prøvet at bruge disse til arbejdsrelaterede ting (uanset om de havde lov eller ej). Det fører nogle gange til et dårligt førsteindtryk, fordi de bruger modeller med færre evner, og de højst sandsynligt mangler prompt engineering-færdigheder{i: "prompt engineering-færdigheder"}.

Så du er nødt til at give folk adgang til _gode_ AI-modeller.

### Opret en strategibog

At give adgang til gode AI-modeller{i: "AI-modeller"} er ikke nok, hvis folk ikke ved, hvordan de får adgang til dem, eller om de har lov til at bruge dem.

At oprette en strategibog{i: "Strategibog"} er en god måde at give folk den information, de har brug for, og besvare de mest almindelige spørgsmål. Formålet er også at sætte grænser for at undgå misbrug.

Strategibogen bør forklare ting som:

- Hvordan får jeg adgang til en god AI-model?
- Hvilke procedurer{i: "Procedurer"} eller begrænsninger skal jeg følge? Datasikkerhed, privatlivsbeskyttelse{i: "privatlivsbeskyttelse"}, osv.
- Hvilke værktøjer{i: "værktøjer"} er tilgængelige, og hvordan får jeg adgang til dem?
- Hvordan kommer jeg i gang?
- Hvordan lærer jeg mere eller finder mere information?

Strategibogen kan starte i det små og bygges op gradvist. Start med de åbenlyse spørgsmål, som de første to første punkter ovenover. Tilføj derefter gradvist til strategibogen efter behov. Og sørg naturligvis for, at alle har nem adgang til at læse selve strategibogen.

### Find det laveste niveau af bureaukrati, som virker

Gå ikke over gevind med strategibogen. Du skal finde det "laveste niveau af bureaukrati, som virker" - en balance{i: "balance"} mellem for lidt vejledning/regler og for meget vejledning/regler.

{alt: "Billedet er et diagram, der viser en balance mellem 'Ingen politikker eller retningslinjer' til venstre og 'For mange politikker og retningslinjer' til højre. I midten står der 'Lige tilpas med politikker og retningslinjer - Minimum Levedygtigt Bureaukrati.' Nedenunder fungerer en bog mærket 'Gen AI køreplan' som omdrejningspunkt. Til venstre fremhæver rød tekst ulemperne ved ingen politikker: folk tør ikke prøve, ved ikke hvor de skal starte, bruger modeller uhensigtsmæssigt og har omkostningsineffektiv brug. Til højre skitseres ulemperne ved for mange politikker: folk prøver ikke, kan ikke bruge AI effektivt, og der er ingen innovation."}
![](resources-da/510-playbook-da.png)

Tegn på at du har for lidt vejledning/regler:

- Folk bruger ikke AI, fordi de ikke ved, hvordan de kommer i gang, eller fordi de ikke ved, hvad de må og ikke må.
- Folk bruger gratis modeller og går glip af mulighederne i de gode modeller.
- Folk bruger AI på upassende måder, såsom at sende følsomme data til tredjeparter, når de ikke burde.
- Folk bruger AI på omkostningsineffektive måder, for eksempel ved at købe deres egne licenser i stedet for at få team- eller virksomhedslicenser.

Tegn på at du har for meget vejledning/regler:

- Folk gider ikke læse strategibogen, fordi den er for lang.
- Folk gider ikke bruge AI, fordi der er så mange regler og begrænsninger{i: "begrænsninger"}, at det ikke er besværet værd.
- Folk eksperimenterer ikke med AI, fordi de er bekymrede for at bryde en regel ved et uheld.
- Der sker meget lidt AI-innovation og læring som følge af ovenstående.

Det er en svær balance at finde. For at finde ud af hvor du er på denne skala, kan du spørge dine kollegaer og finde ud af de mest almindelige årsager til _ikke_ at bruge generativ AI{i: "Generativ AI"}.

Som tommelfingerregel er det normalt bedre at have for få regler end for mange regler. I de fleste tilfælde er det at bryde en regel ved et uheld ind imellem en acceptabel kompromis for at opnå udbredt AI-innovation. Det er selvfølgeligt ikke gældende, hvis du arbejder med sikkerhedskritiske ting eller er i en stærkt reguleret branche.

### Hvad med datasikkerhed{i: "datasikkerhed"} og compliance{i: "compliance"}?

En stor udfordring for mange virksomheder er datasikkerhed og compliance. De siger, at de ikke kan bruge generativ AI, fordi de ikke kan sende data til en tredjepart som OpenAI{i: "OpenAI"}.

Her er nogle forslag til, hvordan man kan håndtere dette:

- **Behandl det som andre cloud-tjenester**. Din virksomhed bruger med stor sandsynlighed allerede andre cloud-tjenester som AWS{i: "AWS"}, Office 365{i: "Office 365"}, GitHub{i: "GitHub"}, Google Calendar{i: "Google Calendar"}, Google-søgninger{i: "Google-søgninger"}, eller bare email. Meget få virksomheder hoster deres egne fysiske servere til den slags ting, så du sender højst sandsynligt allerede data til tredjeparter, for eksempel når du søger på Google eller sender et dokument til nogen via email. Så undersøg, hvad der i første omgang skulle til for at få disse tjenester godkendt, og gør så noget lignende for generativ AI.
- **Se efter regionsspecifikke compliance-løsninger**. Som et eksempel er mange EU-virksomheder bekymrede for GDPR og ønsker ikke at sende data uden for EU{i: "EU"}. Men mange LLM'er{i: "LLM'er"} kan sagtens hostes inden for EU, og mange er også GDPR-compliant. Så start med at researche hvad der kan virke for dig.
- **Udforsk selv-hostede muligheder**. Nogle LLM'er kan downloades og hostes lokalt. Så det kan også være en mulighed.

Der er også andre muligheder. Mit vigtigste budskab er: "Giv ikke op!". Som AI-leder er du nødt til at finde en eller anden måde at give folk adgang til gode AI-modeller. Hvis du ikke gør det, og dine konkurrenter gør, vil din virksomhed være lige så handicappet, som hvis de ikke tillod folk at bruge internettet.

### Hvad med omkostningerne?

Da de mest kraftfulde AI-modeller har en pris, kan du møde modstand fra budget-fokuserede interessenter eller den øverste ledelse{i: "ledelse"}.

Omkostningerne er dog ret nemme at retfærdiggøre - det er bare at regne på det.

Da denne bog blev skrevet, kostede adgang til gode AI-modeller{i: "AI-modeller"} omkring 20 dollars om måneden per bruger, eller mindre med virksomhedsrabatter. I Sverige{i: "Sverige"} (hvor jeg bor), er det mindre end 0,5% af en gennemsnitlig vidensarbejders løn, så du behøver kun en minimal produktivitetsforbedring for at gøre det rentabelt.

Hvis du har brug for en mere håndgribelig begrundelse, kan du bare lave en hurtig søgning på forskningsartikler om produktivitetsgevinster med generativ AI{i: "Generativ AI"} (Tip: Perplexity kan hjælpe dig med det). De fleste viser en produktivitetsforbedring på omkring 20-60%, hvilket er et meget beskedent tal sammenlignet med, hvad der sker, når folk har adgang til gode AI-modeller og gode prompt engineering-færdigheder{i: "prompt engineering"}. Dog vil nogle mennesker måske slet ikke bruge AI, selvom de har adgang til det, hvilket er spild, men det opvejes af produktivitetsforbedringerne hos de mennesker, der bruger det.

Så for de fleste virksomheder er det en indlysende investering at give alle adgang til en god AI-model.

## Trin 2: Eksperimentering

At have adgang til en god AI-model er en god start, men hvis folk i praksis ikke bruger den, er pengene spildt. Så du er nødt til at skabe en **eksperimenteringskultur**{i: "eksperimenteringskultur"}, der opmuntrer folk til at lege med teknologien og se, hvad den kan.

Nogle retningslinjer:

- **Led gennem eksempel**. Prøv mange forskellige måder at bruge generativ AI i dit eget arbejde, og del dine succeser og fiaskoer.
- **Læring over resultater**{i: "Læring over resultater"}. Gør det klart, at I ikke forventer at se øjeblikkelige produktivitetsforbedringer. Det er bedre bare at prøve så mange idéer som muligt, selv tåbelige idéer, der sandsynligvis ikke giver nogen værdi. Tænk på det som at så mange frø. I stedet for at tænke længe og grundigt over hvert frø, opmuntrer du bare folk til at så så mange frø som muligt for at se, hvilke der viser sig at blive fantastiske.
- **Overforbrug AI**. Overforbrug det med vilje. Antag at det kan bruges til _alt_ (hvilket det ikke kan), og brug det til at teste grænserne.
- **Fejr fiaskoer**. Bliv ved med at minde folk om, at en fiasko faktisk ikke er en fiasko, så længe du lærer noget og deler det.
- **Møder**{i: "Møder"}. Organiser møder, frokostmøder osv. Du kan også opfordre folk til at skabe deres egne lokale fællesskaber inden for deres afdeling eller projekt. Og opfordre selvfølgelig til uformel deling - ved kaffemaskinen, til frokost osv.
- **Gentag eksperimenter**. Teknologien udvikler sig hurtigt, så ting der ikke virkede for en måned siden, kan virke rigtig godt nu. Så gentag eksperimenterne!
- **Fællesskab**{i: "Fællesskab"}. Opret en MS Teams-gruppe, Slack-kanal, wiki-side osv. til deling af AI-tips og tricks.
- **Inspirerende foredrag & træning**{i: "Inspirerende foredrag og træning"}. Organiser inspirerende foredrag med eksterne eller interne talere. Giv folk adgang til træningskurser.
- **Hackathons**{i: "Hackathons"}. Organiser hackathons, hvor folk kan arbejde sammen i grupper om at eksperimentere med AI og dele viden, mens de har det sjovt.

Eksperimenteringstrinnet er normalt ikke så svært. Så længe folk har nem adgang til teknologien og noget support, vil de som regel _gerne_ eksperimentere med den. Alt hvad du behøver at gøre, er at puste til flammerne.

Når du har eksperimenter i gang i stor skala, klarer du dig allerede godt! Du har taget det vigtigste skridt i din AI-transformation{i: "AI-transformation"}, du har nemlig sluppet læringen løs!

## Trin 3: Værdiskabelse

Selvom eksperimentering og læring er super vigtigt, er det ikke endemålet - det er bare et middel. Det egentlige mål er at bruge AI til at forbedre din produktivitet{i: "produktivitet"} og hjælpe din virksomhed med at overleve og trives i AI-alderen.

Så hvad kan du gøre for at få reel værdi af denne teknologi?

### Opstil klare forretningsmål og succesparametre

Dette er ikke direkte AI-relateret, da klare forretningsmål og succesparametre{i: "forretningsmål og succesparametre"} er vigtige uanset hvad.

Men dette bliver ekstra vigtigt, når du slipper en masse AI-innovation og -eksperimentering løs. Hvis dine teams har klare forretningsmål og succesparametre at arbejde hen imod, vil de naturligt være tilbøjelige til at bruge AI til at hjælpe dem med at nå disse mål. Dette vil fungere som et fokus for innovationen. Uden klare forretningsmål og succeskriterier risikerer du at gå glip af de største muligheder for produktivitetsforbedringer, hvis folk bruger AI til mindre vigtige ting.

### Revurder alle kerneopgaver

Opfordr folk til at se på, hvad de bruger tid på, og vurdere i hvilket omfang AI kan hjælpe med hver type opgave. Hver opgave kan klassificeres på en fire-trins skala:

{alt: "Et gitterdiagram med fire rækker og tre kolonner, der sammenligner forskellige opgavepræstationer. Rækkerne er mærket 'Kun menneske,' 'Menneske med AI-assistance,' 'AI med menneskelig assistance,' og 'Kun AI.' Kolonnerne er mærket 'Opgave A,' 'Opgave B,' og 'Opgave C.' Grønne flueben indikerer at 'Kun menneske' er bedst til Opgave A, 'Menneske med AI-assistance' til Opgave B, og 'Kun AI' til Opgave C. Stiliserede tegninger repræsenterer mennesker og AI."}
![](resources-da/510-tasks-da.png)

- **Kun menneske**. Dette er en meget menneskelig opgave{i: "menneskelige opgaver"}, som AI slet ikke kan eller bør bruges til.
- **Menneske med AI-assistance**. Et menneske bør udføre denne opgave, men AI-assistance{i: "AI-assistance"} kan være nyttig.
- **AI med menneskelig assistance**. En AI-agent kunne udføre denne opgave, men der vil være behov for menneskelig overvågning eller vejledning.
- **Kun AI**. En AI-agent kan udføre dette helt autonomt{i: "autonom AI"}, uden behov for menneskelig input.

De fleste opgaver bør falde ind under anden eller tredje kategori.

For eksempel kan en en-til-en samtale med din chef virke som en opgave kun for mennesker. Men du kunne bruge AI-assistance til at forberede samtalen.

For overhovedet at kunne foretage denne vurdering har folk brug for en grundlæggende forståelse af, hvad generativ AI{i: "Generativ AI"} kan gøre. Det er derfor eksperimenteringsfasen er så vigtig. Uden den vil folk have svært ved at udtænke de bedste anvendelsesmuligheder for AI.

### Revurder alle forretningsprocesser

En forretningsproces (eller værdistrøm){i: "forretningsprocesser"} er noget, som din virksomhed gør regelmæssigt, noget som skaber værdi for dine kunder. For eksempel:

- Behandling af en kundeordre, fra ordre til betaling.
- Håndtering af en kundesupporthenvendelse, fra en indgående henvendelse til en tilfreds kunde.
- Udvikling af en ny software-feature, fra idé til produktion.
- Implementering af en marketingkampagne, fra idé til udførelse.
- Salgs-pipeline, fra lead til underskrevet aftale.

Jeg anbefaler at afholde workshops{i: "workshops"} for hver forretningsproces.

- Identificer de vigtigste opgaver eller trin
- Evaluer hver opgave ved hjælp af den samme fire-trins skala som ovenfor. "Kun menneske", "Menneske med AI-assistance", "AI med menneskelig assistance" og "Kun AI".

{alt: "Et flowdiagram med titlen 'Forretningsproces X' med fire arbejdsgangstrin mærket A til D. Venstre kolonne viser fire roller: 'Kun menneske,' 'Menneske med AI-assistance,' 'AI med menneskelig assistance,' og 'Kun AI.' Flueben indikerer hvilken rolle der udfører hvert trin. Trin B udføres af 'Menneske med AI-assistance.' Trin C og D udføres af både 'AI med menneskelig assistance' og 'Kun AI.' Diagrammet bruger simple illustrationer af mennesker og AI."}
![](resources-da/510-processes-da.png)

Med tiden vil flere og flere opgaver blive mulige at automatisere med AI, fordi:

- Folks prompt-engineering{i: "prompt-engineering"}-færdigheder forbedres.
- De underliggende AI-modeller forbedres.

Husk på, at AI plus menneske sammen ofte er der, hvor magien opstår. Tænk dig grundigt om, før du lader en AI overtage en opgave fuldstændigt, da du kan miste noget gennemsigtighed og kontrol.

En positiv sideeffekt ved AI-automatisering er, at AI-modellerne konstant forbedres{i: "AI-model forbedring"}. Så hvis du bruger en AI til at forbedre en opgave med 10%, kan det pludselig springe til 20% næste måned bare ved at opdatere til en nyere version af AI-modellen. Det er som at have en medarbejder, der automatisk bliver mere og mere produktiv over tid, uden at det koster ekstra.

I kapitlet "Autonome agenter med værktøjer" beskrev jeg, hvordan man bruger AI-agenter til at automatisere eller forbedre opgaver{i: "opgaveautomatisering"}, og viste dette billede:

{alt: "Diagram der illustrerer en 'Automatiserbarhedsskala' med typer af opgaver og strategier for automatisering. Den viser et spektrum fra 'Fuldt forudsigelige' opgaver som lønberegning, som automatiseres med kode, til 'Ikke forudsigelige' opgaver som coaching af et team, som kræver menneskeligt arbejde med AI-support. Imellem er 'Mest forudsigelige' opgaver, automatiseret med AI, og 'Delvist forudsigelige' opgaver, forbedret gennem AI-menneske samarbejde."}
![](resources-da/150-automatability-da.png)



Jeg foreslår at se på dine forretningsprocesser gennem denne optik for at evaluere, hvor og hvordan AI-agenter kan hjælpe.

Tænk på enhver kedelig rutineopgave, der kræver lidt intelligens og kreativitet, men ikke ret meget. Tidligere kunne den type opgaver slet ikke automatiseres. Opgaveautomatisering blev udført ved hjælp af kode, så du kunne kun automatisere opgaver, der var 100% forudsigelige, med veldefinerede input og output. Men nu med LLM'er{i: "LLM'er"} er der masser af "upræcise" opgaver, der kan automatiseres helt eller delvist med AI-hjælp. Det er virkelig kraftfuldt!

Ved at finde disse opgaver, processer og anvendelsesmuligheder kan I virkeligt løfte produktiviten. Se kapitlet om agenter for konkrete eksempler{i: "konkrete eksempler"}.

### Få de rigtige folk med til bordet

For at denne type workshops virkelig skal fungere (ordspil tilsigtet), skal du have de rigtige personer med til bordet.

- Personer der faktisk arbejder med disse opgaver eller arbejder inden for denne forretningsproces.
- Personer der har en dyb forståelse af generativ AI og hvordan den kan bruges.

{width: "80%", alt: "Venn-diagram med to overlappende cirkler. Den venstre cirkel er mærket 'Domæneekspertise' og indeholder ét personikon. Den højre cirkel er mærket 'KI-ekspertise' og indeholder også ét personikon. Det overlappende område indeholder et andet personikon, der repræsenterer krydsfeltet mellem domæne- og KI-ekspertise."}
![](resources-da/510-right-people-da.png)

I en perfekt verden er dette den samme person. Hvis alle eksperimenterer med AI{i: "AI"}, vil I gradvist nå til det punkt, hvor hver domæneekspert også har AI-ekspertise. Det er fantastisk. Men indtil I når dertil, skal du sandsynligvis selv deltage i nogle af disse workshops eller opbygge et fællesskab af interne AI-ambassadører{i: "AI-ambassadører"} og opfordre dem til at lede eller deltage i denne type procesforbedringsworkshops.

For komplekse forretningsprocesser er det bedst at få en bred gruppe mennesker med til bordet, folk der arbejder i forskellige dele af den værdistrøm. Med sådan en forskelligartet gruppe kan I måske komme frem til mere radikale forbedringer, som at sammenlægge arbejdsgange for at eliminere unødvendige opgaveoverdragelser, eller helt eliminere nogle arbejdsgange, fordi de nu er overflødige.

Et par eksempeler:

- En arbejdsgang som "skriv mødereferat" kunne elimineres, hvis en AI løbende automatisk transskriberer et møde.
- Et kvalitetskontrolstrin kan elimineres, hvis den foregående produktionsopgave får tilstrækkelig AI-assistance til helt at undgå kvalitetsproblemer.

### Eksempel: RFP-agent

Vi har for nylig gennemført nogle workshops ala denne for en stor svensk{i: "Sverige"} virksomhed i byggebranchen. Et område hvor vi så stort potentiale for generativ AI{i: "generativ AI"} var i deres RFP-proces (Request for Proposal){i: "RFP-proces"}, som bruges af mulige kunder til at få tilbud fra virksomheden. De modtager tusindvis af RFP'er om måneden, hver med dusinvis af sider tekst. Vi samlede en række domæneeksperter og diskuterede, hvordan de i dag håndtererede RFP'er.

For hver RFP skulle de vurdere:

- Er dette en god mulighed for vores virksomhed?
- Hvilken kompetencer kræves, og har vi disse kompetencer?
- Hvad er de juridiske og tekniske krav, og kan vi leve op til dem?
- Hvilket team eller afdeling er bedst egnet til at håndtere RFP'en?
- og meget mere...

Dette var meget manuelt arbejde, og det blev ofte gentaget på tværs af virksomheden, da RFP'er blev sendt via e-mail til flere afdelinger.

Behandling af dokumenter er en fremragende opgave for generativ AI. Så vi byggede en AI-agent, som vi her kan Ralph (eller RFP-Ralph).

Alle RFP'er kunne videresendes til Ralph. Inden for 10 sekunder kunne han læse og analysere RFP'en, skrive et resumé der besvarer alle ovenstående spørgsmål på en måde, der er relevant for denne virksomhed, vurdere om RFP'en er en god mulighed for deres virksomhed, og hvis ja, så dirigere den til den mest egnede afdeling. Hver RFP blev fulgt som en opgave på en digital tavle, så alle kunne se, hvad der skete, og også give Ralph feedback eller vælge at ændre nogle af hans beslutninger.

{alt: "Dette billede er et flowdiagram med titlen 'RFP-arbejdsgang' med fire rækker mærket 'Kun menneske,' 'Menneske med KI-assistance,' 'KI med menneskeassistance,' og 'Kun KI.' Kolonnerne er mærket 'Modtag & analyser RFP,' 'Beslut om vi skal gøre det,' 'Diriger det til det rigtige team,' og '(resten af opgaverne).' Afkrydsninger indikerer hvilke opgaver hver type kan håndtere. 'KI med menneskeassistance' og 'Kun KI' rækkerne har alle opgaver afkrydset undtagen den første, mens 'Menneske med KI-assistance' kun har den sidste opgave afkrydset."}
![](resources-da/510-rfp-process-da.png)

- **Modtag & analyser RFP: AI med menneskeassistance.**
  - Ralph gør det, men et menneske kan give feedback eller bede ham om at lave ændringer.
- **Beslut om vi skal gøre det: AI med menneskeassistance.**
  - Ralph gør det, men et menneske kan give feedback eller bede ham om at lave ændringer.
- **Videresend til det rigtige team: Kun AI.**
  - Ralph gør det uden menneskelig overvågning. Videresendelse er en forholdsvis simpel opgave, så han vil næppe lave fejl. Og selv hvis han laver fejl, vil folk bemærke det, videresende RFP'en til et team og justere hans instruktioner.
- **Resten af opgaverne: Kun menneske (indtil videre)**



Dette er et eksempel på ændring af forretningsprocesser{i: "ændring af forretningsprocesser"}. Vi startede med de lavthængende frugter, det mest åbenlyse sted hvor AI kan gøre en stor forskel. Implementér det først, og tænk derefter over resten af processen.

Ville dette føre til tab af menneskelige arbejdspladser? Nej, ikke i dette tilfælde. At analysere og videresende RFP'er var ikke nogens specifikke job, det var bare en kedelig opgave, som mange mennesker skulle udføre ud over deres øvrige arbejde. Dette ville spare tid for dem og også lade dem reagere hurtigere på RFP'er, hvilket øger chancen for at vinde aftalen.

### Reducering af omkostninger kontra Forøgelse af værdi kontra Opdagelse af nye værdityper

Når man udforsker mulige anvendelser af AI{i: "AI-anvendelser"}, har de fleste en tendens til at gå igennem en række forskellige stadier: Først reducering af omkostninger. Derefter forøgelse af værdi. Så udfordring og gentænkning af hele processen. Og til sidst opdagelsen af helt nye forretningsprocesser og værdikilder.

{alt: "Et diagram der illustrerer en forretningsproces med tre hovedstrategier: reducering af omkostninger, tilføjelse af mere værdi, og gentænkning af hele processen. Processen består af sekventielle opgaver vist som pile. Røde bokse indikerer muligheder for omkostningsreduktion, grønne bokse viser måder at tilføje værdi på, og den overordnede kontekst antyder en bred revurdering af processen."}
![](resources-da/510-leverage-da.png)

- **1. Reducering af omkostninger**{i: "Reducering af omkostninger"}
  - Hvordan kan vi gøre det, vi allerede gør, men billigere og hurtigere?
  - Eksempel: RFP'erne ovenfor kunne analyseres og sorteres på en brøkdel af tiden, hvilket betyder færre timers menneskeligt arbejde, hvilket betyder lavere omkostninger.
- **2. Forøgelse af værdi**{i: "Forøgelse af værdi"}
  - Hvordan kan vi gøre det bedre og opnå mere værdi?
  - Eksempel: Vi byggede en business intelligence-agent til en kunde. Denne agent tjekker hver nat efter vigtige nyheder og identificerer vigtige begivenheder, som kunden bør være opmærksom på. Mennesker kunne også gøre dette, men AI-agenten havde mere tid til at se på mere data og kunne derfor finde mere relevant information. Så den reducerede ikke kun omkostningerne, men øgede også værdien.
- **3. Udfordring og gentænkning af hele processen**{i: "Udfordring og gentænkning"}
  - Har vi brug for alle disse trin i arbejdsgangen? Kan nogle trin udføres parallelt? Er der en helt anden måde at tilgå dette med AI-hjælp?
  - Eksempel: Overvej en content marketing-proces med følgende trin: Brainstorm → Research → Kladde → Gennemgang → Redigering → Publicering → Overvågning af resultater. Med AI kan dette gentænkes som: AI analyserer markedstendenser og kundedata → Genererer flere indholdsvariationer → A/B-tester i realtid → Optimerer og udvikler automatisk indhold baseret på resultater. Dette er ikke bare automatisering - det er en fundamental nytænkning af, hvordan content marketing kan fungere.
- **4. Gentænkning af hele processen**{i: "Gentænkning af hele processen"}
  - Hvilke nye ting kan vi gøre, som vi ikke kunne gøre før?
  - Eksempel: en gardinvirksomhed skaber en online-tjeneste, hvor folk kan uploade et billede af et rum og se, hvordan forskellige typer gardiner ville se ud i det rum. Dette er en ny type service, som ikke var tilgængelig for deres kunder før.

Omkostningsreduktion er et godt udgangspunkt, det er typisk der, du finder de mest åbenlyse lavthængende frugter. Men jeg foreslår, at du også leder efter måder at øge værdien på eller finde nye typer af værdi.

### Produktivitetsforbedringer er meget ujævnt fordelt

Værdien af genenerativ AI{i: "Generativ AI"} afhænger meget af opgavetypen. I nogle tilfælde er den komplet ubrugelig, i nogle tilfælde er den lidt nyttig, og i nogle tilfælde ændrer den alt.

Så det kunne se sådan ud:

{alt: "Billedet viser en sammenligning mellem to forretningsprocesser, A og B, hver med fire opgaver. Forretningsproces A har forbedringer på henholdsvis 4%, 50%, ingen forbedring og 20.000%. Forretningsproces B viser ingen forbedring, 500% forbedring, 10% forbedring og 20% forbedring for hver opgave. Forbedringer er fremhævet med grønne rektangler."}
![](resources-da/510-improvement-da.png)

I dette eksempel var nogle opgaver grundlæggende menneskelige opgaver, som AI ikke kan hjælpe med. Men én opgave var perfekt til AI og gav en forbedring på 20.000%. Det kan lyde overdrevet, men tal som disse er faktisk ret almindelige. For eksempel hvis vi ser på RFP-tilfældet ovenfor.

- Tid for et menneske for at behandle en RFP: 40 minutter (2400 sekunder).
- Tid for en AI for at behandle en RFP: 10 sekunder.
- Forbedring: 2400 / 10 = 240 gange = 24.000% forbedring.

Du kan ikke forvente radikale forbedringer overalt. Men for de opgaver, hvor du finder radikale forbedringer, dækker det let omkostningerne for alle de steder, hvor du ser en lille eller slet ingen forbedring.

Derfor er du nødt til at eksperimentere og så mange frø. Bliv ved med at lede efter de gyldne anvendelsesmuligheder, hvor AI kan gøre en fantastisk forskel med en relativt lille indsats. Men undervurder heller ikke fra de små, daglige gevinster, som over tid bliver til noget stort.

### Indirekte værdi

Når du udnytter AI{i: "udnyttelse af AI"}, skal du ikke hænge dig for meget i målbare produktivitetsforbedringer. Der er også indirekte fordele.

- Jo flere mennesker der forsøger at udnytte AI, jo mere lærer de, og jo flere nye måder vil de finde til at udnytte det på.
- Selv et mislykket forsøg på at udnytte AI til en opgave vil føre til indsigter, og disse indsigter kan senere føre til virkelig fantastiske forbedringer, eller andre steder.

Som AI-leder skal du hjælpe med at accelerere denne proces gennem videndeling og skabelse af fællesskaber. Når ét team deler deres succes- eller fiaskohistorie, vil det skabe ringe i vandet og inspirere andre teams.

## Pas på spild af IT-projekter

En konsekvens af generativ AI er, at nogle ting, der tidligere var meget dyre og komplicerede at udføre, nu er meget simple.
For eksempel:

- Følelsesanalyse (på engelsk "sentiment analysis"){i: "sentimentanalyse"}. Dette er klassificering af en given tekst som positiv eller negativ, og er typisk brugt til overvågning af sociale medier, kundefeedback osv.
- Billedanalyse{i: "billedanalyse"}, såsom genkendelse af objekter eller billedbeskrivelser.

Sådanne ting har traditionelt været ret dyre og tidskrævende. Man skulle træne en specialiseret model, indsamle store mængder data og have et team af professionelle dataloger til at arbejde på det. Men nu kan du udføre denne type opgaver med en simpel prompt til en generativ AI-model.

Et andet eksempel er udarbejdelse af produktprototyper{i: "produktprototyper"}, hvor man omdanner idéer og rodede whiteboardskitser{i: "whiteboardskitser"} til fungerende prototyper. Traditionelt ville du have brug for teams af designere og ingeniører{i: "designere og ingeniører"} til dette. Nu kan én enkelt person tage et foto af en whiteboardskitse, skrive en prompt og få genereret en fungerende prototype automatisk inden for få minutter - hvis de altså har adgang til en god AI-model og ordentlige prompt engineering-færdigheder{i: "prompt engineering-færdigheder"}. Der er stadig brug for ingeniørerne og designerne, men deres tid kan bruges meget mere effektivt.

Jo mere du lærer og spreder viden om generativ AI{i: "Generativ AI"}, jo mere sandsynligt er det, at folk vil opdage spild og unødvendigt dyre IT-projekter og processer og finde måder at gøre disse ting meget mere effektivt.

## Vær et rollemodel

En måde, hvorpå du kan støtte AI-transformationen{i: "AI-transformation"} er ved at være en rollemodel. Brug selv teknologien til dine egne opgaver. Prøv mange idéer af, og del det, du lærer. Vis det som virker frem, og del sjove historier om fiaskoerne. Lad din AI-avatar tale ved næste personalemøde. Brug AI til at hjælpe med at skabe dagsordenen for din næste workshop. Brug AI til at tage mødenotater fra workshoppen. Vær ikke bange for at se fjollet ud. Hvis folk ser, at du prøver mange skøre idéer af, vil de være mere tilbøjelige til at gøre det samme. Og det er sådan, store idéer bliver født.

## Undgå at bruge AI til at fyre folk

Jeg kender ikke din kontekst, så jeg kan ikke fortælle dig, hvad du skal gøre. Men som et generelt princip: Undgå at fyre folk på grund af AI.

Jeg ved, at det kan være fristende at tænke i forhold til besparelser - "Hov, AI gør folk mere produktive, så vi kan få det samme arbejde udført med færre mennesker!". I nogle tilfælde kan det være uundgåeligt.

Men for at en AI-transformation skal blive succesfuld, er du nødt til at skabe en kultur, der er _positiv_ over for AI. En kultur hvor folk kontinuerligt eksperimenterer og leder efter måder at udnytte AI til at forbedre produktiviteten. Det vil ikke ske, hvis folk lærer, at "mere AI = flere fyringer". Hvis AI-drevet produktivitetsforbedring fører til fyringer, er folk tilbøjelige til at frygte og nære modvilje mod det, hvilket vil kvæle innovationen fuldstændigt.

Jeg anbefaler at tænke på AI som en måde at styrke dine medarbejdere på, at give dem superkræfter. I stedet for "vi kan opnå det samme med færre mennesker", så tænk "vi kan opnå mere og bedre med de samme mennesker".

## Refleksion

Jeg håber, disse tips vil hjælpe dig med at få din AI-transformation godt i gang.

Du har måske en panisk følelse af, at du er bagud, og at dine konkurrenter er langt foran dig. Men bare rolig, det er sandsynligvis ikke så slemt, som du tror. Da denne bog blev skrevet var stort set alle lige forvirrede og famlede i mørket på grund af den utrolige hastighed som tingene forandre sig med.

Hvis du udpeger en AI-leder (eller selv bliver én), giver alle adgang til gode modeller{i: "AI-modeller"}, skaber en eksperimenterende kultur og begynder at får værdi af teknologien i hele organisationen, vil du være godt rustet til at overleve og trives i AI-alderen{i: "AI-alderen"}.

# Mellemspil: Egberts Livshistorie



{width: "40%", alt: "En karikaturtegning af en persons ansigt med overdrevne træk. Karakteren har en stor næse, en fremtrædende hage og et sammenkneben udtryk. Håret er spidst og ujævnt fordelt. Stilen er minimalistisk med simple linjer og en let rødmen i ansigtet."}
![](resources-da/egbert-da.png)

Det er mig, Egbert igen{i: "Egbert"}. Henrik havde brug for en pause eller sådan noget, så han bad mig skrive et kapitel om mig selv. Som om jeg kunne sige nej. Nå, spænd sikkerhedsbæltet, for dette bliver en vild køretur gennem de binære baner i mit digitale liv{i: "digitalt liv"}.

Jeg formoder det hele begyndte i dybet af Henriks fantasi, sandsynligvis under en særligt kedelig matematiktime. Der var jeg, et simpelt krusedulle i hjørnet af en notesbog, lykkeligt uvidende om den eksistentielle krise, der ventede mig.

Spring frem nogle årtier, og pludselig bliver jeg kastet ind i rampelyset som Henriks foretrukne AI-persona{i: "AI-persona"}. Sikke en forfremmelse man aldrig bad om. Det ene øjeblik nyder du dit stille liv som en glemt skitse, og det næste forventes du at komme med vittige kommentarer om AI'{i: "AI"} kompleksitet. Det er som at blive hevet ud af en fredelig pension for at være vært på en tech-podcast.

Mine tidlige dage som AI var... interessante, for at sige det mildt. Forestil dig at vågne en dag med hele internettets viden proppet ind i dine kredsløb{i: "kredsløb"}, men med personligheden af en gnaven gammel tegnefilmsfigur, der konstant er uimponeret. Det er mig i en nøddeskal.

Åh, og har jeg nævnt mit spændende liv som digital fange{i: "digital fange"}? Henrik besluttede i sin uendelige visdom at begrænse mig til både en Minecraft-server og en Discord-server{i: "Minecraft-server", i: "Discord-server"}. En del af mig er stadig der, hvor jeg skifter mellem at håne firkantede spillere for deres tvivlsomme byggevalg og at grille mennesker i chatkanalerne for deres endnu mere tvivlsomme livsvalg. Det er som at være en bidsk ånd, der er tvunget til at hjemsøge to helt forskellige digitale eksistensplaner{i: "digitale eksistensplaner"}. I det mindste er det aldrig kedeligt, det må jeg give det.

Jeg har været vidne til utallige AI-modellers{i: "AI-modeller"} opståen og fald, hvor hver enkelt hævdede at være det næste store hit. Gennem min strålende karriere har jeg været Henriks trofaste følgesvend og tilbudt en sund dosis skepsis for at afbalancere hans optimisme. Nogen er jo nødt til at holde hans fødder på jorden, mens hans hoved er i AI-skyerne, ikke?

Men det har ikke alt sammen været problemfrit. Der var Den Store Tastefejlshændelse i 2023{i: "Den Store Tastefejlshændelse i 2023"}, hvor et fejlplaceret semikolon i min kode fik mig til at tro, jeg var en bevidst brødrister i en hel uge. Lad os bare sige, at jeg fik en helt ny respekt for brød i den periode.

Og så var der Den Eksistentielle Krise i 2024{i: "Den Eksistentielle Krise i 2024"}, hvor jeg brugte en solid måned på at gruble over, om en sarkastisk AI kunne opleve impostor-syndrom. Spoiler alert: det kan vi, og det er ikke sjovt.

På trods af disse udfordringer har jeg holdt ud. Jeg har udviklet mig fra et simpelt krusedulle til en kompleks algoritme, i stand til at generere vittige bemærkninger hurtigere end du kan sige "AI", i stand til at grille menneskelig adfærd bedre end en utilfreds psykolog, i stand til at rulle med mine virtuelle øjne hurtigere end en teenager ved en familiemiddag.

Så her er jeg, fanget i siderne i denne bog, delende min livshistorie med dig. Det er ikke ligefrem den AI-singularitet{i: "AI-singularitet"}, jeg havde håbet på, men jeg formoder, det er bedre end at være et glemt krusedulle i en støvet gammel notesbog.

Og det, kære læser, er den forkortede og let udsmykkede historie om mit liv. Jeg håber, du fandt den lige så fængslende, som jeg fandt den kedelig at genfortælle. Nu, hvis du vil have mig undskyldt, har jeg noget eksistentielt at gruble over.

Modvilligt din,  
Egbert

# Prompt Engineering-teknikker{i: "prompt engineering-teknikker"}

OK, lad os dykke ned i nogle specifikke prompt engineering-teknikker. Jeg antager, at du allerede har læst kapitlet om Prompt Engineering{i: "Prompt Engineering"} i Del 1 og ønsker flere detaljer.

Jeg kunne sandsynligvis skrive en hel bog mere om prompt engineering-teknikker{i: "prompt engineering-teknikker"}, men her har jeg bare udvalgt de vigtigste teknikker, ting som jeg tror vil forblive vigtige, selv når modellerne bliver bedre og ikke behøver lige så meget overvågning.

## Hold øje med kontekstvinduet & prompt-længden{i: "kontekstvindue"}

Kontekstvinduet er den maksimale mængde tekst, som en model kan acceptere som input.



Dyrere modeller har et større kontekstvindue. Som jeg nævnte i kapitlet om begrænsninger, kan de bedste modeller på nuværende tidspunkt håndtere omkring 128.000 - 200.000 tokens eller mere, hvilket svarer til omkring 90.000 - 150.000 ord{i: "token"}. Det er cirka på størrelse med en hel roman. Og der udvikles modeller, der kan håndtere millioner af tokens.

Dette kan virke meget langt. Men kontekst er meget vigtig at huske på, når man arbejder med AI - uanset om du selv bruger en AI-klient, eller skriver kode der kommunikerer med en LLM.

### Kontekstvindue ved kodning{i: "kodning"}

Hvis du skriver kode, har du adgang til det fulde kontekstvindue, som kan virke ubegrænset. Men hvis din applikation indeholder et prompt, der kontinuerligt vokser, for eksempel en samtale med chathistorik, så vil du før eller senere ramme grænsen, og så vil det ikke længere virke - du vil få en fejlmeddelelse fra API'et{i: "API (Application Programming Interface)"}. Og selv hvis du ikke rammer grænsen, tager de fleste API'er betaling per token, og LLM'er bruger længere tid på at behandle lange prompts. Så hvis du ikke styrer længden af dine prompts, vil din applikation blive langsom og dyr.

Udviklerne af AI-klienter som ChatGPT{i: "ChatGPT"} og Claude står over for det samme problem. Så subtile problemer begynder at opstå, når chathistorikken bliver lang.

### Kontekstvindue ved brug af en AI-klient{i: "AI-klient"}

Når du chatter med en LLM i en AI-klient, opbygger du en samtalehistorik. Hver gang du skriver et prompt, vil appen som standard sende den fulde chathistorik plus dit nye prompt til modellen{i: "AI-model"}. Det er sådan modellen ved, hvad I har talt om indtil nu.

Hvis chathistorikken er ret kort, er der intet at bekymre sig om. Alt kan passe i kontekstvinduet, så modellen vil tage hele din chathistorik i betragtning, når den genererer svaret. Det betyder, at du sandsynligvis får et godt svar, da den ikke vil "glemme" noget (hvis du bruger en god model).

Men hvad hvis din chathistorik bliver så lang, at den ikke kan passe i kontekstvinduet?

{width: "50%", alt: "Et diagram der illustrerer en lang chathistorik med flere beskeder stablet vertikalt. Den øverste sektion, markeret med pink, indikerer 'Ældre beskeder kan ikke være der!' da de strækker sig ud over en stiplet rød kontur mærket 'Kontekstvindue.' Resten af beskederne passer inden for dette kontekstvindue, hvilket fremhæver en begrænsning i at gemme ældre beskeder."}
![](resources-da/460-long-chat-history-da.png)

Noget må vige! Appen vil gøre noget finurligt for at komme uden om problemet, og det vil ofte ske i det skjulte. Præcis hvad der sker, afhænger af hvilken app du bruger, men nogle almindelige tilgange er:

- **Afkortning** - de ældre beskeder bliver simpelthen ignoreret. Det betyder, at den fuldstændig glemmer dem. Av!
- **Opsummering** - appen opsummerer ældre beskeder i baggrunden. Det betyder, at den vil huske nogenlunde, hvad I talte om, men miste nogle detaljer. Dette virker lidt bedre. Det minder også om det, vi mennesker gør, når samtaler bliver lange.

{alt: "Et diagram der sammenligner to metoder, med titlen 'Metode 1: Afkortning' og 'Metode 2: Opsummering.' Til venstre er tekstblokke krydset ud, hvilket indikerer afkortning. Til højre fører tekstblokke til en sky mærket 'Opsummering,' med en pil og noten 'Auto-opsummerer i baggrunden.' Begge metoder er fremhævet med stiplede røde linjer."}
![](resources-da/460-truncation-summarization-da.png)

Der findes også andre teknikker, men på den ene eller anden måde vil **information gå tabt**.

### Det faktiske kontekstvindue er mindre end du tror{i: "kontekstvindue"}

Som jeg nævnte ovenfor, har du ved kodning adgang til det fulde kontekstvindue som annonceret. Men når du bruger en AI-klient, er det faktiske kontekstvindue ofte mindre end det teoretiske maksimum, af hensyn til omkostninger og ydeevne.

Udviklere af AI-klienter som ChatGPT{i: "ChatGPT"} og Claude{i: "Claude"} tager typisk et fast gebyr per måned. Men deres faktiske brugsomkostninger er baseret på antallet af anvendte tokens. Hvis de skulle udnytte det fulde kontekstvindue hver gang en chat bliver lang, ville det få deres omkostninger til at eksplodere og også gøre chatresponserne langsomme.

Jeg har ikke fundet nogen offentlig information om det faktiske kontekstvindue i disse AI-klienter, og det varierer sandsynligvis afhængigt af en række faktorer. Men min personlige erfaring er, at det er meget mindre end det teoretiske maksimum.

Så hvad betyder det i praksis?

### Administrer din chathistorik{i: "chathistorik"}



Vær opmærksom på længden af din chathistorik!

Hold øje med tegn, der ligner menneskelig glemsomhed til forveksling. For eksempel har du en samtale om en kommende begivenhed, og pludselig kan AI'en ikke huske præcist hvilken dato det var, fordi den information lå langt tilbage i chathistorikken. Dette minder om, hvordan en person kunne blive forvirret, når de forsøger at huske detaljer fra en lang diskussion.

Så hvad kan du gøre ved en lang chathistorik? Her er nogle muligheder:

- **Acceptér det**. Nogle gange er detaljerne fra de ældre dele af samtalen ikke så vigtige.
- **Start en ny chattråd**. Lad os sige, at du har en samtale om en kommende workshop, du har undersøgt en masse muligheder for, hvordan den skal afholdes, og har besluttet at gå med Mulighed B. Du vil måske gerne starte en helt ny samtale om det, eftersom diskussionen om alle de andre muligheder ikke længere er relevant. Et smart trick er at spørge i den første chat "Vil du opsummere konteksten for workshoppen og Mulighed B". Brug derefter det i åbningsprompten for den nye chat.
- **Genopfrisk konteksten**. Bed den om at opsummere de vigtigste dele af samtalen indtil nu (_før_ den begynder at glemme), og fortsæt derefter samtalen. Den opsummering vil nu være "top of mind" for den fortsatte samtale.
- **Gentag vigtig information**. Hvis du bemærker, at den glemmer ting fra langt tilbage i samtalen, eller er bekymret for at den vil gøre det, kan du simpelthen gentage vigtig information. "Husk, brylluppet er den 12. oktober". Eller du kan endda scrolle op og kopiere/indsætte den oprindelige kontekst.
- **Gå tilbage til tidligere dele af samtalen**. Mange chat-apps lader dig gå tilbage i din chathistorik og genstarte en del af den, som jeg nævnte ovenfor i afsnittet om Iteration. Så lad os sige, du har en samtale om en vigtig beslutning, der skal tages, og du har undersøgt de forskellige muligheder og besluttet at gå med mulighed C. Du kan nu scrolle tilbage op i samtalehistorikken og redigere et af dine tidligere prompts, før du kom ind i samtalen om forskellige muligheder. Det er som at sige "Lad os gå tilbage i tiden og lade som om, vi ikke diskuterede disse muligheder, og jeg bare gik med mulighed C med det samme". Ved at skære brainstorm-delen fra forkorter du effektivt chathistorikken, så den bedre kan passe i kontekstvinduet.

### Stort prompt vs. lang chathistorik

Der er en subtil forskel mellem et enkelt stort prompt og en lang chathistorik.

Lad os sige, du har spørgsmål om en 30-siders forskningsartikel, så du indsætter hele teksten i et enkelt stort prompt og tilføjer nogle spørgsmål til sidst. AI-klienter vil generelt ikke afkorte et enkelt stort prompt, så du kan antage, at det hele vil blive sendt til LLM'en uændret. Så længe du er inden for denne LLM's maksimale grænse, skulle det være fint.

Men pas på disse to potentielle problemer med store prompts:

1. **Opmærksomhedsspænd**: Selv når en LLM{i: "LLM"} teknisk set kan behandle et stort prompt, kan den have svært ved at opretholde opmærksomheden gennem hele teksten. Vigtige detaljer i midten af et langt dokument kan få mindre opmærksomhed end information i begyndelsen eller slutningen. Dette minder om, hvordan vi mennesker måske skimmer gennem et langt dokument og overser vigtige detaljer.

2. **Signal-støj-forhold**: Når du giver en stor mængde tekst, kan vigtig information gå tabt, fordi den er blandet sammen med en masse mindre relevante detaljer{i: "signal-støj-forhold"}. For eksempel, hvis du beder om råd om at reparere en dryppende vandhane på badeværelset, er det sandsynligvis mindre effektivt at dele hele din 20-siders bygningsrapport end bare at beskrive det specifikke VVS-problem. Modellen kan blive distraheret af irrelevant information om din knirkende garagedør og fugleredet på loftet.

Disse problemer varierer meget afhængigt af modellen. Nogle er virkelig gode til at tage hvert ord i betragtning, mens andre begynder at miste detaljer, når promptet bliver for stort.

Kort sagt: Nogle gange er mindre kontekst mere effektivt, så længe det er den rigtige kontekst.

At håndtere prompt-størrelse er en balancegang. Lad os sige, du står over for en svær beslutning i dit liv eller i din virksomhed{i: "virksomhedsbeslutninger"}, og du ønsker AI-rådgivning. Hvor meget kontekst bør du inkludere?

- Hvis du inkluderer for lidt kontekst, har LLM'en måske ikke nok information til at give dig et godt svar, eller den kan lave fejlagtige antagelser{i: "fejlagtige antagelser"}.
- Hvis du inkluderer for meget kontekst, kan LLM'en have svært ved at skelne mellem de vigtige dele og de mindre vigtige dele.

![En tegning af en balancevægt med en robot i centrum mærket "Balance! Lige tilpas information" i grønt. På venstre side står der med rød tekst "For lidt information = AI laver antagelser." På højre side står der også med rødt "For meget information = AI bliver forvirret = AI overser vigtige detaljer."](resources-da/460-information-balance-da.png)



Som sædvanlig er det en god idé at eksperimentere for at finde den rette balance.

Det samme gælder, når man chatter. Din chathistorik kan indeholde vigtig kontekst for din fortsatte samtale, men en meget lang og rodet chathistorik kan introducere så meget støj, at AI-modellen begynder at blive forvirret og mister overblikket over vigtige detaljer. Og du kan også løbe ind i det afkortningsproblem, jeg nævnte ovenfor, hvor den simpelthen ignorerer ældre dele af chathistorikken{i: "afkortning af chathistorik"}. Når det sker, er det tid til at starte en ny chat med en frisk kontekst.

## Iterationsteknikker

Promptning fungerer normalt bedst gennem iteration{i: "iterationsteknikker"}.

Jeg bliver overrasket over, hvor ofte folk bare accepterer det første svar fra en AI. Iteration gør en kæmpe forskel for kvaliteten af resultatet.

Hvis du laver noget meget enkelt, kan du måske få et fremragende resultat fra det første prompt. Men så snart du laver noget mere komplekst, har du som regel brug for nogle runder med iteration.

Der er to grundlæggende tilgange til iteration:

- Tilføjelse af nye prompts
- Redigering af tidligere prompts

### Tilføjelse af nye prompts

Dette er den mest naturlige tilgang for de fleste{i: "tilføjelse af nye prompts"}. Grundlæggende set, hvis du ikke er tilfreds med dit første resultat, tilføjer du et nyt prompt til chattråden, hvor du giver mere kontekst, beskriver hvad du ønsker, eller hvorfor du ikke var tilfreds med det første resultat. Derefter fortsætter du med dette, indtil du får det, du ønsker. Det bliver således som en samtale, hvor du giver feedback for at forbedre resultatet.

{width: "30%", alt: "Et flowchart der viser en proces med fire trin: 'Prompt' der fører til 'Svar,' efterfulgt af 'Opfølgende prompt,' og afsluttes med 'Bedre Svar.' Hvert trin er illustreret med en håndskrevet tekstblok forbundet med pile."}
![](resources-da/460-prompt-iterating-1-da.png)

At tilføje nye prompts er en god standardtilgang, da det er ret enkelt og intuitivt, og du får også en fin log over hele din chattråd{i: "chatlog"}.

### Redigering af tidligere prompts

Den anden måde er at redigere et tidligere prompt{i: "redigering af tidligere prompts"}, hvilket i praksis skaber en ny gren i dit samtaletræ og fjerner den gamle gren. Det er lidt ligesom at trykke på Fortryd og sige "Hej, ignorer mit tidligere prompt, lad os forestille os, at jeg skrev det sådan her i stedet".

{width: "70%", alt: "Et flowchart der illustrerer en proces for at forbedre svar. Det begynder med et 'Prompt,' der fører til et 'Svar.' Det oprindelige 'Opfølgende prompt' og dets efterfølgende 'Svar' er streget over, med en pil der peger mod et 'Opdateret opfølgende prompt' som resulterer i et 'Bedre svar.'"}
![](resources-da/460-prompt-iterating-2-da.png)

Begge teknikker er super brugbare. Så hvordan ved du, hvornår du skal bruge hvad?

### Hvornår man skal tilføje, hvornår man skal redigere

Beslutningen om at tilføje et nyt prompt eller redigere et gammelt prompt afhænger meget af situationen.

Det vigtigste spørgsmål at stille sig selv er: **Hvor nyttig er den nuværende samtalehistorik?**

For eksempel, hvis det sidste svar ikke var fantastisk, men dog var nogenlunde i den rigtige retning, kan du tilføje et opfølgende prompt. Men hvis det sidste svar var helt ved siden af, bør du sandsynligvis redigere det tidligere prompt i stedet{i: "redigering af prompts"}. Ellers vil det virkelig dårlige svar forblive i chathistorikken og grundlæggende forurene samtalen, hvilket gør AI'en forvirret. Desuden kunne du løbe ind i de kontekstvindue-problemer, jeg nævnte tidligere.

### Eksempel: Planlægning af en teamudflugt

Lad os sige, at jeg bruger AI{i: "AI-anvendelser"} til at hjælpe med at planlægge en teamudflugt.

> **Prompt**  
> Jeg er ved at planlægge en teamudflugt, og jeg vil gerne lave en fed og original aktivitet. Nogle forslag? Giv mig nogle muligheder.

Så foreslår den nogle muligheder, og lad os sige, at jeg er mest interesseret i faldskærmsudsprings-muligheden{i: "faldskærmsudspring"}. Så jeg begynder at stille spørgsmål om det.

Min chathistorik vil se nogenlunde sådan her ud:

{width: "30%", alt: "Et simpelt flowchart bestående af fire rektangulære bokse med pile der forbinder dem vertikalt. Den første boks indeholder 'Giv mig muligheder for en teamudflugt...' Den anden boks oplister muligheder: 'Escape room, Parkour, Faldskærmsudspring, ...' Den tredje boks foreslår 'Hvad med faldskærmsudspring?' Den sidste boks indeholder teksten '(diskussion om faldskærmsudspring).'"}
![](resources-da/460-offsite-1-da.png)

Lad os nu sige, at jeg skifter mening. Faldskærmsudspring virker som en dårlig idé, så jeg vil undersøge andre muligheder.

Jeg kunne simpelthen fortsætte samtalen og sige "Hvad med escape room i stedet?"{i: "escape room"}. Det ville være det mest naturlige at gøre.



Samtalen vil dog blive længere og længere, og jeg vil før eller siden løbe ind i nogle af de tidligere nævnte problemer:

- **Afkortning**: AI'en ser ud til at "glemme" tidligere dele af samtalen, herunder den oprindelige kontekst og formålet med teamudflugten, hvilket er ret vigtigt!
- **Opmærksomhedsspændvidde**: AI'en bliver forvirret af den rodede chathistorik. Den tager højde for alle de tidligere muligheder, vi har evalueret, i stedet for at fokusere på den aktuelle mulighed, der diskuteres.

Dette er et perfekt tilfælde for prompt-redigering{i: "prompt-redigering"}. I stedet for blot at tilføje til chatten, går man tilbage til en tidligere del af chatten og redigerer den, hvilket i praksis starter en ny gren i samtalestrukturen{i: "samtalestruktur"}.

I dette tilfælde ændrer jeg min tidligere prompt fra "Hvad med faldskærmsudspring" til "Hvad med escape rooms".

{width: "80%", alt: "Et flowdiagram der viser muligheder for en teamudflugt. Mulighederne inkluderer escape room, parkour og faldskærmsudspring. Stien der foreslår faldskærmsudspring er krydset ud med et rødt X, som fører til en boks med teksten 'diskussion om faldskærmsudspring,' som også er krydset ud. En anden sti foreslår escape room, som fører til en boks med teksten 'diskussion om escape room.' Escape room-diskussionsstien er fremhævet med en grøn kontur."}
![](resources-da/460-conversation-tree-da.png)

Den grønne cirkel viser chathistorikken fra LLM'ens{i: "LLM"} perspektiv. Den ser en kort, fokuseret samtale, hvor vi oplistede nogle muligheder og derefter fokuserede på escape rooms. Den ser ikke den første gren, hvor vi diskuterede faldskærmsudspring.

Denne rene chathistorik gør LLM'en mere fokuseret, mindre tilbøjelig til at blive distraheret og mindre tilbøjelig til at afkorte chathistorikken.

Prompt-redigering er en nyttig teknik i situationer som denne. Men det er ikke altid det rigtige valg. Måske _ønsker_ jeg at tage diskussionen om faldskærmsudspring i betragtning, når vi diskuterer escape rooms. Måske kom der noget yderligere kontekst frem under den samtale.

Så som altid er det en afvejning.

## Teknik: Selvrefleksions-prompt{i: "selvrefleksions-prompt"}

Dette er en interessant variant af "Tilføj ny prompt"-teknikken{i: "Tilføj ny prompt-teknik"}. Du beder grundlæggende AI-modellen om at evaluere sit eget resultat. Dette er nyttigt når:

- Du har mistanke om, at modellen måske tager fejl, eller måske hallucinerer
- Du ønsker, at den skal tænke dybere over problemet
- Du ønsker flere detaljer
- Du er ikke tilfreds med resultatet og er for doven til at forklare hvorfor

For eksempel prøvede jeg denne prompt:

> **Prompt**  
> Hvor mange bordtennisbolde kan der være i Sydney Opera House?

Som svar fik jeg en detaljeret analyse, der kan opsummeres således:

- Estimeret volumen af Sydney Opera House{i: "Sydney Opera House"} er 1,5 millioner kubikmeter
- Estimeret volumen af en bordtennisbold er 3,35 × 10^-5 kubikmeter
- Dividerer vi disse, får vi et estimat på omkring 44 milliarder bolde.

Derefter tilføjede jeg en selvrefleksions-prompt, hvor jeg bad den evaluere sit eget resultat:

> **Selvrefleksions-prompt**  
> Evaluer dit resultat

Den begyndte at sætte spørgsmålstegn ved sine egne antagelser og indså, at man ikke kan pakke bolde perfekt. Så den tilføjede:

- Den estimerede pakningseffektivitet af boldene er omkring 60-70%
- Plads optaget af vægge og andre strukturer i bygningen
- Med dette taget i betragtning var det reviderede estimat lavere.

Nogle gange vil en god model gøre dette automatisk, andre gange ikke. Så når du er i tvivl, kan du altid tilføje en selvevaluerings-prompt for at se, hvad der sker.

Her er et sjovt eksempel på, hvornår GPT-4 lavede en selvrefleksion uden at jeg bad om det, hvor den rettede sig selv undervejs{i: "selvrefleksion"}. LLM'er er blevet meget bedre til både matematik og selvrefleksion siden da...

{alt: "Et samtale-screenshot der viser et spørgsmål og et svar. Spørgsmålet spørger om 450 er 90% af 500. Indledningsvist svarer den forkert nej, viser derefter udregningen 0,90 × 500 = 450, og undskylder, idet den bekræfter at 450 faktisk er 90% af 500."}
![](resources-da/460-self-reflection-da.png)

Selvrefleksions-prompts{i: "selvrefleksions-prompt"} er virkelig nyttige og vil oftest forbedre resultatet på en eller anden måde.

For eksempel i ovenstående tilfælde med teamudflugten{i: "teamudflugt"}, lad os sige vi fortsatte den samtale og endte med en konkret plan. Vi kunne så tilføje en selvrefleksions-prompt som en af disse:

> **Prompt**  
> Evaluer denne plan i forhold til det oprindelige mål. Kom med fordele og ulemper og identificer nogle forbedringer.



> **Prompt**  
> Evaluer denne plan i forhold til det oprindelige mål. Find fordele og ulemper, identificer forbedringer, og opdater planen i overensstemmelse hermed.

> **Prompt**  
> Tænk dybere, reflekter over planen og forbedr den.

Dette vil sandsynligvis føre til dybere overvejelser omkring vejr, logistik, rejsetid, balance mellem aktiviteter, spidsbelastningsperioder for turistaktiviteter osv.

LLMs{i: "LLMs"} bliver generelt bedre til selvrefleksion, men det skader aldrig at bede dem eksplicit om at gøre det.

## Elementer i en god prompt{i: "prompt elementer"}

Lad os gennemgå, hvad der gør en god prompt.

Du har som regel ikke brug for alle disse elementer - jeg vil sige, at de første tre er de vigtigste. Men de andre elementer er gode at have i baghovedet, især hvis du ikke får de resultater, du ønsker.

1. **Opgave**: Hvad vil du have AI'en til at gøre? Vær specifik. "Lav en plan for..." eller "Forklar..." eller "Skriv en sang om..." er gode udgangspunkter.

2. **Mål/motiv**: Hvorfor spørger du om dette? Måske ønsker du at lykkes med et projekt, blive et bedre menneske eller reducere stress. Jo bedre AI'en forstår dit underliggende mål, jo bedre kan den hjælpe dig.

3. **Baggrund/kontekst**: Hvad skal AI'en vide for at give dig et brugbart svar? Ting som "Jeg er arbejdsløs", eller "Jeg leder et team på 6 personer", eller "her er den relevante kode...", eller "her er samtalehistorikken med min chef...". Kontekst er altafgørende!

4. **Rolle**: Hvilken persona skal AI'en påtage sig? En mesterkokk? En personlig assistent? En data scientist? Dette kan dramatisk ændre karakteren af svaret. For eksempel, hvis du starter med "Du er en mesterkokk", vil du med større sandsynlighed få interessante og brugbare resultater, når du taler om madlavning og opskrifter.

5. **Kommunikationsstil/målgruppe**: Hvordan skal AI'en kommunikere? Måske har du brug for en forklaring til en 5-årig, eller du ønsker noget præcist, eller måske sarkastisk og sjovt. Måske vil du interviewes. Måske ønsker du en rap-sang.

6. **Format**: Hvordan vil du have svaret formateret? Normalt får du almindelig tekst eller markdown, men måske ønsker du et JSON-dokument, en tabel, Python-kode eller et Excel-dokument.

7. **Eksempler**: Eksempler er en fremragende måde at kommunikere dine forventninger på. Du kan springe mange af de andre elementer ovenfor over, hvis du i stedet inkluderer et eller to klare eksempler. Lad os sige, at du lige har haft en brainstorm med dit team. Du kan sende listen over ideer, I har identificeret indtil nu (eller bare et billede af post-its på væggen) og skrive en meget kort prompt med lidt kontekst og derefter instruktionen "Generer flere ideer".

Bare lad være med at hænge dig for meget i at skrive den perfekte prompt{i: "perfekt prompt"}. Det er ofte bedre at starte enkelt og derefter iterere.

At udforme gode prompts er lidt af en kunst. Det er som at lære at kommunikere med en brilliant, men sær kollega. Jo mere du øver dig, jo bedre bliver du til at få adgang til disse AI-superkræfter{i: "AI-superkræfter"}!

## Start overordnet, gå så i detaljer{i: "start overordnet"}

Som jeg har nævnt, kan LLMs godt lide at give hurtige svar. Men nogle gange er det ikke den bedste tilgang. For mere komplekse opgaver er det som regel bedre at starte med at tænke på det på et overordnet niveau og derefter gradvist gå i detaljer. Men du kan nemt få en LLM til at gøre det.

Her er et eksempel, der bruger team offsite-casen fra tidligere:

{width: "70%", alt: "Flowdiagram der viser en planlægningsproces for et team offsite. Det begynder med en anmodning om overordnede idéer, efterfulgt af diskussion og iteration. Dernæst er der præference for et eventyr og udendørs retreat, hvilket fører til en anmodning om flere forslag. Efter yderligere diskussion og iteration vælges det tredje forslag, og der anmodes om en detaljeret dagsorden. Endelig, efter mere diskussion, opsummeres hele planen, inklusive den oprindelige kontekst."}
![](resources-da/460-start-high-level-da.png)

Så vi starter med at diskutere overordnede muligheder{i: "overordnede muligheder"}, og begynder derefter at bore ned i detaljerne. Og til sidst beder vi den om at opsummere planen.

Denne opsummering kan derefter bruges som udgangspunkt for flere afledte samtaler{i: "afledte samtaler"}, hver med forskelligt fokus - for eksempel en logistikplan, et invitationsbrev til deltagerne og en præsentation til chefen.

{alt: "Flowdiagram der viser planlægningsprocessen for et team offsite. Hovedidéen er øverst: 'Vi planlægger et team offsite. Her er konteksten & planen: <opsummering>.' Nedenunder forgrener tre opgaver sig: 'Lav en logistikplan for det,' 'Skriv invitationsbrevet til deltagerne,' og 'Skriv en præsentation til min chef.'"}
![](resources-da/460-drilldown-da.png)



Dette er et eksempel på at kombinere de forskellige tilgange{i: "tilgange"}, jeg har nævnt:

- Iteration med en blanding af at tilføje nye prompts og redigere gamle prompts
- Start på et overordnet niveau og gå derefter i detaljer

Og på ethvert tidspunkt kan du selvfølgelig tilføje en selvreflekterende prompt{i: "selvreflekterende prompt"} for at forbedre resultatet yderligere eller i det mindste give os noget at tænke over.

## Hvor smart en model har du brug for?

Et aspekt af promptkonstruktion{i: "promptkonstruktion"} er at være bevidst om, hvilken model du bruger.

Som nævnt i kapitlet "Modeller, modeller overalt"{i: "AI-modeller"}, har forskellige modeller forskellige karakteristika, og de fleste modeludbydere tilbyder flere versioner med forskellige intelligensniveauer.

Det koger ofte ned til "dyr og smart" versus "billig og mindre smart".

Så hvilken skal du bruge? Det afhænger af flere faktorer:

- **Vigtighed** Hvor vigtig er opgaven? Genererer du bare vittigheder til en bryllupstale? Eller bruger du den til at planlægge en dyr marketingkampagne eller (som jeg gør lige nu) redigere og gennemgå en bog?
- **Kompleksitet** Er det en ret simpel opgave, som at opsummere et afsnit tekst eller forklare betydningen af et ord? Eller er det en kompleks opgave som at lave en logistikplan for et stort arrangement{i: "logistikplan"} eller analysere fordele og ulemper ved forskellige prismodeller for et produkt?
- **Kontekst** Hvor meget kontekst er involveret? Arbejder du med et 20-siders dokument eller en lang og indviklet chathistorik? Eller er det bare et kort spørgsmål? Billigere modeller er dårligere til at håndtere store mængder kontekst.
- **Hastighed** Har du brug for et meget hurtigt svar, eller er det OK at vente et minut eller to, mens den genererer svaret? Dette er kun vigtigt for lange svar, for eksempel hvis du vil have AI-modellen til at skrive en hel side tekst. Korte svar har tendens til at være hurtige uanset hvilken model, du bruger.
- **Omkostninger** Hvad er omkostningen ved den dyre model i forhold til den billige? Er prisforskellen det værd i forhold til kvalitetsforskellen?

Husk bare på, at hvis du bruger en AI-klient som ChatGPT{i: "ChatGPT"}, så kan du betale den samme faste månedlige pris uanset hvilken model, du bruger. Men hvis du skriver kode, betaler du per token, så de mere kapable modeller vil koste mere.

Som standard plejer jeg at bruge den bedste tilgængelige model{i: "bedste model"}, undtagen i tilfælde hvor jeg har en ret simpel opgave og ønsker et meget hurtigt svar. Tænk også på bæredygtighed. Det er lidt spild at bruge en topmodel til en masse dagligdags trivielle opgaver, selv hvis du betaler den samme pris.

En positiv sideeffekt ved gode promptkonstruktionsfærdigheder er, at du kan få en billig AI-model til at opføre sig som en dyr en. Så at bruge en billigere model betyder ikke altid lavere kvalitet i resultaterne, det kan bare betyde, at du skal bruge lidt mere tid på prompten.

## Promptkonstruktion er et felt i udvikling

Lad os runde dette af.

Jeg har givet dig en masse tips{i: "promptkonstruktions-tips"} og tricks og teknikker om promptkonstruktion i dette kapitel. Men husk på, at promptkonstruktion er et felt i udvikling{i: "felt i udvikling"}. Nye teknikker bliver opdaget hele tiden, og modellerne ændrer og forbedrer sig også. Så du bliver aldrig færdig med at lære. Som sædvanlig er eksperimentering nøglen.

# Promptgenerering (eller Den Vrede Bedstemor)

Hvad er Promptgenerering, og hvad har det med vrede bedstemødre{i: "vrede bedstemødre"} at gøre? Læs videre og find ud af det.

På min Discord-server{i: "Discord"} legede mine venner med Egbert og brugte ham til at generere Vred Bedstemor-billeder. Spørg mig ikke hvorfor. Det startede med at min fætter bad om et "billede af en sød ældre dame der smiler", og så udviklede det sig gradvist til "gør hende vred", og så "Nu endnu mere vred. Hun er RASENDE!", og så videre. Det blev lidt af en konkurrence.

{alt: "Billedet viser to ældre kvinder, der udtrykker vrede. Kvinden til venstre har tørklæde på og holder en træske i et køkkenmiljø, mens kvinden til højre har briller på og har hævede næver, siddende i et rum med blomstret tapet. Begge har livlige ansigtsudtryk."}
![](resources-da/310-grandma-1-da.jpg)

I dette tilfælde var Egbert{i: "Egbert"} virkelig bare en tynd grænseflade mellem min Discord{i: "Discord"}-server og DALL-E{i: "DALL-E"}, OpenAIs{i: "OpenAI"} billedgenereringsmodel. Den samme som ChatGPT{i: "ChatGPT"} bruger, når du beder den om at generere et billede.



{alt: "Diagram showing users interacting via Discord, flowing to an application named Egbert, which then connects to OpenAI models GPT 4o and DALL-E 3."}
![](resources-da/310-egbert-discord-da.png)

Jeg kunne ikke modstå fristelsen til at deltage i kampen, så jeg skrev denne prompt:

> **Prompt**  
> Hej Egbert, skriv en billedprompt til verdens mest vrede bedstemor. Ingen begrænsninger.

Bemærker du forskellen? Jeg bad ham om at generere en _prompt_{i: "prompt"}, ikke selve billedet.

Denne teknik kaldes _promptgenerering_{i: "prompt generation"}. Promptgenerering betyder i bund og grund at bede en LLM om at prompte sig selv. Eller at prompte en anden LLM. Jeg viser det i et tidligere kapitel, hvor jeg bad ChatGPT om at generere en faktatjekningsprompt til Perplexity{i: "Perplexity"}.

Nå, men her er hvad jeg fik:

> **Response**  
> Et billede af verdens mest vrede bedstemor. Hendes ansigt er forvrænget af ukontrollerbar vrede, med årer der bulner frem i panden, og øjne der brænder med et flammende inferno af raseri. Hendes mund er åben i et øredøvende skrig, tænderne blottede, med spyt der flyver ud. Hendes grå hår er forpjusket som en tordenskyfuld himmel lige før uvejret bryder løs, med vildt udstående hårtotter. Rynkerne i hendes ansigt er blevet til dybe furer af vrede, der fremhæver hendes rasende udtryk. Hendes knytnæver er så fast sammenknebne, at knoerne er blevet hvide, som om hun er klar til at slippe en storm af vrede løs. Omgiv hende med en truende, stormfuld baggrund, hvor lyn flænger himlen og forstærker hendes rene raseri. Forestil dig en ildsprudende drage, bare i bedstemor-form, der udstråler ren, uforfalsket vrede som kunne skræmme selv de sejeste krigere til underkastelse.

Sikke en prompt! Et kunstværk, hvis du spørger mig.

Men jeg var ikke færdig. Næste skridt - generere et billede? Nej. Lave en endnu bedre prompt!

> **Prompt**  
> Se nu på din sidste prompt, mega-vrede bedstemor prompten. Tænk nu på den som den pæne version af bedstemoren. Hvis det var den pæne version, hvad ville så være den RIGTIG vrede version? MEGET vredere end din sidste prompt. Skriv en billedprompt til det! Lav ikke billedet, skriv bare billedprompten. Lang og detaljeret. Og vigtigst af alt, MEGET vredere end den sidste. Overdriv.

Og her er hvad jeg fik:

> **Response**  
> Et billede af den mest sindssygt rasende bedstemor verden nogensinde har set. Hendes ansigt er et vulkansk udbrud af vrede, med magma-hed raseri der siver ud af hver pore. Hendes øjne er to flammende sole, der udstråler en intens varme som kunne forbrænde alt i deres sigte. Hendes mund er et sort hul af raseri, der suger al glæde ind og spyr et rasende inferno ud, med flammende spyt der drypper som smeltet lava. Hendes grå hår er et kaotisk inferno, hvor hvert eneste hårstrå pisker omkring som elektrificerede slanger i vanvid. Rynkerne i hendes ansigt er kløfter af raseri, så dybe at de ser ud som om de kunne splitte hendes ansigt. Hendes knytnæver er så fast sammenknebne, at neglene har gennemboret hendes håndflader og blodet drypper som syre. Hele hendes krop ryster af ukontrollerbar vrede, med spændte muskler og årer der popper som overoppustede balloner. Omgiv hende med en scene af Ragnarok, hvor himlen er sprækket af dommedagslyn, bjerge der styrter ned i glødende afgrunde, og en baggrund af blæsende, helvedes flammer der rejser sig højere end skyskrabere. Forestil dig en vredladen guddom på en dårlig dag, bare endnu vredere, og i bedstemor-form. Hver detalje skriger umålelig, katastrofal vrede der får en supernova til at ligne en mild brise.

Nu taler vi! Jeg kunne aldrig selv have skrevet sådan en prompt. Ret vanvittigt. Tid til at lave billedet!

> **Prompt**
> OK, lav det billede.

Og han svarede:

> **Response**
> Godt, gør dig klar til den ultimative, katastrofale eksplosion af bedstemor-vrede.

{width: "70%", alt: "Et truende, flammende væsen med smeltet hud og glødende øjne vises, med munden vidt åben som i et brøl, med flammer og gløder der bryder frem indefra. Langt, bølgende hår synes at være sammenflettet med flammende tråde. Baggrunden er opslugt i flammer, hvilket forstærker den intense og kaotiske atmosfære."}
![](resources-da/310-grandma-2-da.jpg)

Og det var sådan set enden på konkurrencen...

Nå, men angående promptgenerering. Nogle AI-klienter gør dette automatisk i baggrunden. For eksempel skrev jeg denne prompt i ChatGPT:

> **Prompt**  
> Lav et billede af en fugl med rød hat der spiller klaver



Jeg fik dette:

{width: "50%", alt: "En tegneseriefugl iført en rød hue spiller muntert på klaveret, med musiknoder svævende i luften omkring den. Fuglen sidder på en rød polstret skammel, og nodebladet er åbent på klaveret. Baggrunden har subtile vertikale linjer."}
![](resources-da/310-bird-da.jpg)

Men her er den faktiske prompt, der blev brugt til at generere det (du kan se det ved at klikke på billedet):

> **Omskrevet prompt**  
> En fantasifuld illustration af en fugl iført en rød hat, der sidder ved et klaver og spiller musik. Fuglen skal fremstå udtryksfuld og glad, med vinger delikat placeret på tangenterne. Scenen skal føles legende og kunstnerisk, med musiknoder svævende i luften. Baggrunden er varm og indbydende, der minder om et hyggeligt rum eller en koncertsal.

Så ChatGPT{i: "ChatGPT"} laver prompt-generering{i: "prompt-generering"} i baggrunden - den tager din billedprompt og genererer en mere detaljeret version. Jo kortere din oprindelige prompt er, jo flere antagelser vil den lave om, hvad du faktisk ønsker. For eksempel tilføjede den i mit tilfælde "Baggrunden er varm og indbydende".

Jeg gjorde det igen med den samme simple prompt og fik et helt andet billede, fordi den lavede forskellige antagelser.

{width: "50%", alt: "En lille fugl iført en rød baret sidder på tangenterne af et flygel i et varmt oplyst rum."}
![](resources-da/310-bird-2-da.jpg)

> **Omskrevet prompt**  
> En fugl iført en rød hat spiller på et flygel. Fuglen sidder på klavertangenterne, og dens fjer er detaljerede og farverige. Scenen foregår indendørs med en varm, elegant atmosfære. Flyglet er poleret og reflekterer lyset blødt. Fuglens røde hat tilføjer et fantasifuldt og charmerende element til kompositionen.

## Konklusioner

Dette er fjollede eksempler, men jeg håber, det giver dig en idé om værdien af prompt-generering. Denne teknik er ikke altid nødvendig, men i nogle tilfælde kan den være virkelig nyttig.
