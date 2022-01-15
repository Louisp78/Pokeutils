from enum import Enum


class Type(Enum):
    NORMAL = 0
    FEU = 1
    EAU = 2
    PLANTE = 3
    ELECTRIK = 4
    GLACE = 5
    COMBAT = 6
    POISON = 7
    SOL = 8
    VOL = 9
    PSY = 10
    INSECTE = 11
    ROCHE = 12
    SPECTRE = 13
    DRAGON = 14
    TENEBRE = 15
    ACIER = 16


# Init type_matrix
w, h = 17, 17
type_matrix = [[1 for x in range(w)] for y in range(h)]

# Complete type_matrix

# NORMAL
type_matrix[Type.NORMAL.value][Type.ROCHE.value] = 0.5
type_matrix[Type.NORMAL.value][Type.SPECTRE.value] = 0
type_matrix[Type.NORMAL.value][Type.ACIER.value] = 0

# FEU
type_matrix[Type.FEU.value][Type.FEU.value] = 0.5
type_matrix[Type.FEU.value][Type.EAU.value] = 0.5
type_matrix[Type.FEU.value][Type.ROCHE.value] = 0.5
type_matrix[Type.FEU.value][Type.DRAGON.value] = 0.5
type_matrix[Type.FEU.value][Type.POISON.value] = 2
type_matrix[Type.FEU.value][Type.GLACE.value] = 2
type_matrix[Type.FEU.value][Type.INSECTE.value] = 2
type_matrix[Type.FEU.value][Type.ACIER.value] = 2

# EAU
type_matrix[Type.EAU.value][Type.EAU.value] = 0.5
type_matrix[Type.EAU.value][Type.PLANTE.value] = 0.5
type_matrix[Type.EAU.value][Type.DRAGON.value] = 0.5
type_matrix[Type.EAU.value][Type.FEU.value] = 2
type_matrix[Type.EAU.value][Type.SOL.value] = 2
type_matrix[Type.EAU.value][Type.ROCHE.value] = 2
# PLANTE
type_matrix[Type.POISON.value][Type.FEU.value] = 0.5
type_matrix[Type.POISON.value][Type.POISON.value] = 0.5
type_matrix[Type.POISON.value][Type.POISON.value] = 0.5
type_matrix[Type.POISON.value][Type.VOL.value] = 0.5
type_matrix[Type.POISON.value][Type.INSECTE.value] = 0.5
type_matrix[Type.POISON.value][Type.DRAGON.value] = 0.5
type_matrix[Type.POISON.value][Type.ACIER.value] = 0.5
type_matrix[Type.POISON.value][Type.EAU.value] = 2
type_matrix[Type.POISON.value][Type.SOL.value] = 2
type_matrix[Type.POISON.value][Type.ROCHE.value] = 2

# ELECTRIK
type_matrix[Type.ELECTRIK.value][Type.SOL.value] = 0
type_matrix[Type.ELECTRIK.value][Type.POISON.value] = 0.5
type_matrix[Type.ELECTRIK.value][Type.ELECTRIK.value] = 0.5
type_matrix[Type.ELECTRIK.value][Type.DRAGON.value] = 0.5
type_matrix[Type.ELECTRIK.value][Type.EAU.value] = 2
type_matrix[Type.ELECTRIK.value][Type.VOL.value] = 2

# GLACE
type_matrix[Type.GLACE.value][Type.FEU.value] = 0.5
type_matrix[Type.GLACE.value][Type.EAU.value] = 0.5
type_matrix[Type.GLACE.value][Type.GLACE.value] = 0.5
type_matrix[Type.GLACE.value][Type.ACIER.value] = 0.5
type_matrix[Type.GLACE.value][Type.POISON.value] = 2
type_matrix[Type.GLACE.value][Type.SOL.value] = 2
type_matrix[Type.GLACE.value][Type.VOL.value] = 2
type_matrix[Type.GLACE.value][Type.DRAGON.value] = 2

# COMBAT
type_matrix[Type.COMBAT.value][Type.SPECTRE.value] = 0
type_matrix[Type.COMBAT.value][Type.POISON.value] = 0.5
type_matrix[Type.COMBAT.value][Type.VOL.value] = 0.5
type_matrix[Type.COMBAT.value][Type.PSY.value] = 0.5
type_matrix[Type.COMBAT.value][Type.INSECTE.value] = 0.5
type_matrix[Type.COMBAT.value][Type.NORMAL.value] = 2
type_matrix[Type.COMBAT.value][Type.GLACE.value] = 2
type_matrix[Type.COMBAT.value][Type.ROCHE.value] = 2
type_matrix[Type.COMBAT.value][Type.TENEBRE.value] = 2
type_matrix[Type.COMBAT.value][Type.ACIER.value] = 2

# POISON
type_matrix[Type.POISON.value][Type.ACIER.value] = 0
type_matrix[Type.POISON.value][Type.POISON.value] = 0.5
type_matrix[Type.POISON.value][Type.SOL.value] = 0.5
type_matrix[Type.POISON.value][Type.ROCHE.value] = 0.5
type_matrix[Type.POISON.value][Type.SPECTRE.value] = 0.5
type_matrix[Type.POISON.value][Type.PLANTE.value] = 2

# SOL
type_matrix[Type.SOL.value][Type.VOL.value] = 0
type_matrix[Type.SOL.value][Type.PLANTE.value] = 0.5
type_matrix[Type.SOL.value][Type.INSECTE.value] = 0.5
type_matrix[Type.SOL.value][Type.FEU.value] = 2
type_matrix[Type.SOL.value][Type.ELECTRIK.value] = 2
type_matrix[Type.SOL.value][Type.POISON.value] = 2
type_matrix[Type.SOL.value][Type.ROCHE.value] = 2
type_matrix[Type.SOL.value][Type.ACIER.value] = 2

# VOL
type_matrix[Type.VOL.value][Type.ELECTRIK.value] = 0.5
type_matrix[Type.VOL.value][Type.ROCHE.value] = 0.5
type_matrix[Type.VOL.value][Type.ACIER.value] = 0.5
type_matrix[Type.VOL.value][Type.PLANTE.value] = 2
type_matrix[Type.VOL.value][Type.COMBAT.value] = 2
type_matrix[Type.VOL.value][Type.INSECTE.value] = 2

# PSY
type_matrix[Type.VOL.value][Type.INSECTE.value] = 0
type_matrix[Type.VOL.value][Type.PSY.value] = 0.5
type_matrix[Type.VOL.value][Type.ACIER.value] = 0.5
type_matrix[Type.VOL.value][Type.COMBAT.value] = 2
type_matrix[Type.VOL.value][Type.POISON.value] = 2

# INSECTE
type_matrix[Type.INSECTE.value][Type.FEU.value] = 0.5
type_matrix[Type.INSECTE.value][Type.COMBAT.value] = 0.5
type_matrix[Type.INSECTE.value][Type.POISON.value] = 0.5
type_matrix[Type.INSECTE.value][Type.VOL.value] = 0.5
type_matrix[Type.INSECTE.value][Type.SPECTRE.value] = 0.5
type_matrix[Type.INSECTE.value][Type.ACIER.value] = 0.5
type_matrix[Type.INSECTE.value][Type.PLANTE.value] = 2
type_matrix[Type.INSECTE.value][Type.PSY.value] = 2
type_matrix[Type.INSECTE.value][Type.TENEBRE.value] = 2

# ROCHE
type_matrix[Type.ROCHE.value][Type.COMBAT.value] = 0.5
type_matrix[Type.ROCHE.value][Type.SOL.value] = 0.5
type_matrix[Type.ROCHE.value][Type.ACIER.value] = 0.5
type_matrix[Type.ROCHE.value][Type.FEU.value] = 2
type_matrix[Type.ROCHE.value][Type.GLACE.value] = 2
type_matrix[Type.ROCHE.value][Type.VOL.value] = 2
type_matrix[Type.ROCHE.value][Type.INSECTE.value] = 2

# SPECTRE
type_matrix[Type.SPECTRE.value][Type.NORMAL.value] = 0
type_matrix[Type.SPECTRE.value][Type.TENEBRE.value] = 0.5
type_matrix[Type.SPECTRE.value][Type.ACIER.value] = 0.5
type_matrix[Type.SPECTRE.value][Type.PSY.value] = 2
type_matrix[Type.SPECTRE.value][Type.SPECTRE.value] = 2

# DRAGON
type_matrix[Type.DRAGON.value][Type.ACIER.value] = 0.5
type_matrix[Type.DRAGON.value][Type.DRAGON.value] = 2

# TENEBRE
type_matrix[Type.TENEBRE.value][Type.COMBAT.value] = 0.5
type_matrix[Type.TENEBRE.value][Type.TENEBRE.value] = 0.5
type_matrix[Type.TENEBRE.value][Type.ACIER.value] = 0.5
type_matrix[Type.TENEBRE.value][Type.PSY.value] = 2
type_matrix[Type.TENEBRE.value][Type.SPECTRE.value] = 2

# ACIER
type_matrix[Type.ACIER.value][Type.FEU.value] = 0.5
type_matrix[Type.ACIER.value][Type.EAU.value] = 0.5
type_matrix[Type.ACIER.value][Type.ACIER.value] = 0.5
type_matrix[Type.ACIER.value][Type.GLACE.value] = 2
type_matrix[Type.ACIER.value][Type.ROCHE.value] = 2






