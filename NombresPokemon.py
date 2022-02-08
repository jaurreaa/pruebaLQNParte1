"""
    Take the following selection of 70 English Pokemon names (extracted from Wikipedia's list of Pokemon), and generate
    the/a sequence with the highest possible number of Pokemon names where the subsequent name starts with the final
    letter of the preceding name. No Pokemon name is to be repeated.
"""

names = '''audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'''.split()

longest_list, current_list = [], []

# Devuelve el índice de la siguiente palabra que comienza con la última letra de la palabra anterior
def return_index_next_word(lastletter, names):
    for index, name in enumerate(names):
        if name.startswith(lastletter):
            return index
    return False

for name in names:
    current_name = name
    current_list.append(current_name) # Añadir el primer nombre a la lista

    namelist = names[:] # copia de la lista de nombres
    namelist.pop(namelist.index(current_name)) # Eliminar el primer nombre de la lista

    index = return_index_next_word(current_name[-1], namelist) # Obtener el índice del siguiente nombre

    # Siempre y cuando haya un nombre que comience con la última letra de la palabra anterior
    while index is not False:
        current_name = namelist[index] # Obtener este nombre
        current_list.append(current_name) # Agrégalo a la lista actual
        namelist.pop(index) # Eliminarlo de la lista
        index = return_index_next_word(current_name[-1], namelist) # Obtener el indice del siguiente

    # Si la lista actual > la lista mas larga, actualizarla
    if len(current_list) > len(longest_list):
        longest_list = current_list

    # Vaciar lista actual para el próximo ciclo
    current_list = []

print(longest_list)