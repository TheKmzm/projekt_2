# projekt_2
Tic-tac-toe

Cílem této hry je umístit 3 hrací kameny (křížek X nebo kolečko O), a to horizontálně, vertikálně nebo diagonálně. Jde o hru pro dva hráče (příp. počítač).
Program musí splňovat tyto požadavky:

Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:
Ukázka kódu2

    """
    
    projekt_2.py: druhý projekt do Engeto Online Python Akademie
    
    author: 
    
    email: 
    
    discord: 
    
    """

    import ...

program pozdraví uživatele,
vypíše v krátkosti pravidla hry,
zobrazí hrací plochu,
vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene,
pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní,
pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní,
pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené
jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy,
program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří,
pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu,
zápis organizovaný do krátkých a přehledných funkcí.

Úvodní text:

    Welcome to Tic Tac Toe
    ========================================
    GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row
    ========================================
    Let's start the game

Příklad fungujícího kódu:

    Welcome to Tic Tac Toe
    ============================================
    GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row
    ============================================
    Let's start the game
    --------------------------------------------
    +---+---+---+
    | | | |
    +---+---+---+
    | | | |
    +---+---+---+
    | | | |
    +---+---+---+
    ============================================
    Player o | Please enter your move number: 5
    ============================================
    +---+---+---+
    | | | |
    +---+---+---+
    | | O | |
    +---+---+---+
    | | | |
    +---+---+---+
    ============================================
    Player x | Please enter your move number: 1
    ============================================
    +---+---+---+
    | X | | |
    +---+---+---+
    | | O | |
    +---+---+---+
    | | | |
    +---+---+---+
    ============================================
    Player x | Please enter your move number:
    ...
    ============================================
    Player o | Please enter your move number:
    ============================================
    +---+---+---+
    | X | | |
    +---+---+---+
    | | O | |
    +---+---+---+
    | | | |
    +---+---+---+
    ============================================
    Congratulations, the player o WON!
    ============================================
