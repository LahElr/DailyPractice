from collections import defaultdict
from functools import wraps
from time import time,time_ns

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func:{f.__name__} took: {(te-ts):2.4f} sec')
        return result
    return wrap


class ViolateSolution:
    r'''
    Complexity = O(`len(text)*len(pattern)`)
    '''
    @timing
    def strStr(self, haystack: str, needle: str) -> int:
        ptr_h = 0
        ptr_n = 0

        len_h = len(haystack)
        len_n = len(needle)
        while True:
            if ptr_n >= len_n:
                return ptr_h-ptr_n
            if ptr_h >= len_h:
                return -1
            if haystack[ptr_h] == needle[ptr_n]:
                ptr_h += 1
                ptr_n += 1
            else:
                if ptr_n == 0:
                    ptr_h += 1
                else:
                    ptr_h-=(ptr_n-1)
                    ptr_n=0

    def findLast(self, pattern, suffix_start) -> int:
        ptr_s = -1
        ptr_p = -2
        pattern_len = len(pattern)
        while True:
            if pattern_len+ptr_s<suffix_start:
                return pattern_len+ptr_p+1
            if pattern_len+ptr_p<0:
                return -1
            
            if pattern[ptr_p] == pattern[ptr_s]:
                ptr_s-=1
                ptr_p-=1
            else:
                if ptr_s == -1:
                    ptr_p-=1
                else:
                    ptr_p += (-ptr_s-2)
                    ptr_s = -1

class BoyerMooreSolution:
    r'''
    Complexity = O(`len(pattern)+len(text)*len(pattern)`)
    ended slower than `ViolateSolution` as the calculation of good suffix moving need O(`len(pattern)`)
    but average complexity is O(n+m)

    '''
    @timing
    def strStr(self,text: str, pattern: str) -> int:
        pattern_position = 0
        pattern_len = len(pattern)
        pattern_pointer = pattern_len-1
        text_len = len(text)
        violate_solver = ViolateSolution()

        char_last_position_in_pattern = defaultdict(lambda :-1)
        for i,ch in enumerate(pattern[::-1]):
            if char_last_position_in_pattern[ch] == -1:
                char_last_position_in_pattern[ch] = pattern_len-1-i

        def bad_char():
            return pattern_pointer-char_last_position_in_pattern[text[pattern_position+pattern_pointer]]

        def good_suffix():
            # pattern_pointer to the char before first position of good suffix
            # i.e.: good suffix == pattern[pattern_pointer+1:] == text[pattern_position+pattern_pointer+1]
            # find the position of last good suffix
            if pattern_pointer +1 >= pattern_len:
                return 0
            last_good_suffix_position = -1
            for ptr in range(pattern_pointer+1,pattern_len):
                # last_good_suffix_position = violate_solver.strStr(pattern,pattern[ptr:])
                last_good_suffix_position = violate_solver.findLast(pattern,pattern_pointer+1)
                if last_good_suffix_position == ptr or last_good_suffix_position == -1:
                    continue
                else:
                    break
            # print(f"<gs-<{pattern_pointer},{last_good_suffix_position}")
            if last_good_suffix_position > pattern_pointer:
                last_good_suffix_position = -1
            return pattern_pointer+1-last_good_suffix_position
        
        while True:
            if pattern_pointer <0:
                return pattern_position
            if pattern_position+pattern_pointer>=text_len:
                return -1
            
            # print(f"{pattern_position}+{pattern_pointer}->{text[pattern_position+pattern_pointer]};{pattern[pattern_pointer]}")

            if text[pattern_position+pattern_pointer] == pattern[pattern_pointer]:
                pattern_pointer-=1
            else:
                # print(bad_char(),good_suffix())
                moving_dist = max(bad_char(),good_suffix(),1)
                pattern_pointer = pattern_len-1
                pattern_position+= moving_dist


# text = "mississipi"
# pattern = 'issip'
# text = "babbbbbabb"
# pattern = 'bbab'
text='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla faucibus odio lorem, vitae lobortis nisi eleifend non. Morbi ac diam mollis, eleifend libero ultricies, ultrices velit. Duis sapien massa, pharetra et blandit et, viverra in lorem. Maecenas ut elementum mauris, quis porttitor massa. Fusce venenatis non dolor vel blandit. Morbi consectetur ligula magna, at porta nibh pharetra eget. Nulla et varius risus.
Nulla viverra sem vitae vestibulum rhoncus. In lacinia suscipit ante, quis molestie magna posuere nec. Nunc accumsan laoreet aliquam. Nam quis augue nec orci consequat semper. Aenean ligula mauris, mattis et metus a, pellentesque ultricies nisl. Sed cursus egestas arcu, vel iaculis purus sodales eget. Pellentesque lectus libero, auctor in viverra suscipit, ullamcorper id nisi. Pellentesque ac sem libero. Nunc ultricies tincidunt molestie. Nunc vehicula metus at nulla accumsan, nec ultricies orci eleifend. Nunc aliquet, sapien ac ornare convallis, turpis mi feugiat ipsum, mollis consectetur arcu urna cursus tortor. Nullam porta cursus pellentesque. Morbi vel lectus in arcu vulputate facilisis. Morbi a arcu quis justo suscipit ultrices eget non orci. Morbi ultricies ex ligula, posuere suscipit metus interdum a. Vestibulum rutrum non risus aliquam eleifend.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam venenatis, ex et tincidunt sagittis, est odio placerat dui, sed molestie ligula metus et ligula. Nunc facilisis ut ligula bibendum tincidunt. Vivamus iaculis et risus sed euismod. Proin feugiat faucibus massa, non tempus mi volutpat vitae. Morbi ultrices eros purus, in pellentesque nibh semper a. Phasellus augue justo, mollis convallis augue ut, pretium scelerisque orci. Fusce ullamcorper ornare lectus. Vivamus vitae mauris eget purus malesuada molestie. Mauris faucibus orci ac mattis ornare. Ut pulvinar, nibh at ultricies tempus, sapien justo pretium neque, quis ultrices lacus libero sed mi.
Donec dolor tortor, vehicula ac pellentesque vitae, scelerisque in orci. Morbi aliquam sapien eu lobortis fermentum. Suspendisse interdum vulputate dolor id rhoncus. Vestibulum facilisis sed ipsum laoreet pharetra. Pellentesque vitae consectetur elit. Praesent euismod ac eros eu rhoncus. Donec sagittis hendrerit ligula, nec lobortis neque dictum vel. Fusce ullamcorper mauris sed facilisis tincidunt. Fusce vitae erat mi. Morbi sollicitudin ornare interdum. Donec mi nisi, gravida eget luctus sed, maximus vitae lacus. Mauris quis dui porta, sagittis erat vel, pretium sem.
Sed eu maximus enim. Pellentesque at mauris ex. Praesent eget ipsum nec justo rhoncus semper. Fusce feugiat nulla et justo tincidunt posuere. Donec sit amet enim placerat, finibus enim ac, tristique justo. Duis vel diam ut magna venenatis pulvinar eu id ante. Nulla scelerisque gravida vulputate. Suspendisse convallis in tellus non mattis. Donec vitae risus ultricies, fringilla neque ut, semper nisl. Duis rutrum accumsan tincidunt. Nullam vulputate eget turpis eu ultricies. Maecenas pharetra enim nisl, a dignissim erat pretium eget. Quisque fermentum tincidunt velit, in venenatis urna fringilla id.
Cras sed lacus at erat gravida iaculis et sed metus. Vivamus nisl eros, mollis vitae ultricies ut, bibendum sed orci. Proin non tellus magna. Donec iaculis elit in accumsan ullamcorper. Suspendisse ultricies sollicitudin ullamcorper. Mauris nec dui diam. Sed viverra, arcu at mollis molestie, augue quam mollis felis, ac tempor justo justo eget lectus. Praesent convallis urna ex, tincidunt venenatis ligula sollicitudin eget. Ut a cursus orci.
Ut nec dolor id felis laoreet euismod vitae nec urna. Nam sollicitudin sapien eu ligula pellentesque, a rutrum leo interdum. Vivamus pretium non erat quis dignissim. In eget erat non elit condimentum dictum. Morbi quis ligula vitae metus semper tempus a in libero. Sed pharetra porta blandit. Mauris lacus nisi, rhoncus sed mattis blandit, euismod ac nulla. Donec massa orci, pulvinar ac dui nec, dictum vulputate enim. Sed gravida risus eu metus placerat tempus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum at mattis dolor, at porta libero. Mauris finibus sapien vel luctus sodales. Suspendisse interdum diam ac orci vehicula, ut consectetur elit pretium. Sed condimentum lectus eu vestibulum auctor. Proin purus diam, interdum vel mi vel, vehicula tempus nibh.
Cras rhoncus orci eu nulla auctor, ut sodales leo bibendum. Pellentesque luctus lacus ut nisi ultrices sollicitudin. Nam at dui in eros tincidunt pellentesque eu in nisi. Morbi imperdiet ipsum nulla, vitae condimentum orci volutpat sit amet. Quisque massa metus, rutrum at vehicula ac, posuere eu elit. Praesent bibendum interdum lacinia. Sed vitae condimentum ante. Nam eu purus finibus, facilisis lorem et, pellentesque enim. Sed lacinia ullamcorper turpis quis blandit. Morbi mi magna, dapibus vitae facilisis vitae, maximus quis tellus. Maecenas laoreet, turpis sed iaculis rhoncus, neque dolor varius enim, id venenatis elit ante a leo. Nulla aliquet congue est, id lobortis purus sagittis sed. Cras aliquam tempus congue.
Sed id diam fringilla libero ullamcorper pharetra. Cras iaculis mauris vel semper auctor. Maecenas egestas elit mi, sit amet iaculis ligula feugiat vel. Etiam sed risus iaculis, pharetra arcu ac, elementum urna. Donec et pharetra magna. Sed ac lorem dignissim ligula ullamcorper scelerisque. Aenean iaculis sodales tellus, non ullamcorper ex venenatis non. Integer ullamcorper arcu ut est rutrum rhoncus. Donec tristique enim felis, vel elementum purus pellentesque at. Aliquam malesuada in nunc eget mollis. Nam ultricies arcu in dolor mollis vulputate.
Quisque eget hendrerit purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sapien justo, tincidunt ac nisl quis, rutrum ornare velit. Ut massa metus, maximus in est non, fermentum convallis dolor. Donec sit amet dolor congue, lacinia augue id, ultricies dui. Vestibulum eros leo, eleifend a hendrerit nec, mollis eget urna. Ut pharetra at sem ac commodo. Donec eget suscipit mauris. Sed in placerat dui, quis tristique tellus. Proin in pellentesque justo, a consectetur nisl. Donec quis cursus nisi. Nunc urna dolor, elementum a consectetur nec, dapibus id massa. Fusce nec lacus enim.
Praesent luctus ex eu nulla fringilla, quis sollicitudin magna tristique. Aliquam cursus euismod nunc, vel interdum lectus tristique nec. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas auctor lobortis tempus. Quisque velit justo, pulvinar pellentesque malesuada nec, consectetur ac est. Suspendisse augue diam, accumsan nec cursus eget, tempor a lectus. Mauris sed imperdiet sem, in lobortis arcu. In purus mauris, dictum vitae elementum vel, imperdiet et eros. Etiam dignissim volutpat augue, a feugiat enim aliquet vitae. Vivamus sollicitudin facilisis libero a bibendum. Proin tincidunt tempor pharetra. Nunc non metus odio. Nulla viverra eget lorem id iaculis.
Nam malesuada vehicula est, at consectetur felis mattis cursus. Mauris finibus vulputate nulla nec semper. Donec egestas nisl lectus, a fermentum justo scelerisque id. Nullam sagittis commodo nisl sed luctus. Praesent a viverra quam, quis bibendum tellus. Maecenas faucibus eleifend magna at consectetur. Etiam sed auctor diam. Sed eget volutpat arcu, sed malesuada dolor. Praesent pretium tincidunt ligula non euismod. Morbi pharetra dignissim metus non consectetur. Maecenas et porta urna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec quis venenatis nunc, id tincidunt ipsum.
In hac habitasse platea dictumst. Phasellus quis lorem non mi pharetra congue. Aenean interdum ornare volutpat. Sed at augue sit amet turpis vulputate finibus. Nullam non enim ut nisl euismod dictum in sit amet eros. Duis et fringilla odio, in pulvinar enim. Maecenas facilisis bibendum augue, eu congue nibh eleifend vel. Fusce tincidunt purus lorem, at bibendum nibh lacinia vitae. Ut finibus dapibus justo. Vivamus commodo cursus neque, non faucibus lacus. Phasellus id sem sed augue euismod placerat. Morbi mollis egestas rutrum. Morbi sed gravida mi. Morbi convallis lobortis est nec pellentesque.
Vivamus ut mauris id tellus cursus rhoncus non ac dui. Ut felis felis, condimentum a tempor ut, malesuada quis sapien. Fusce finibus est nec eros rhoncus, quis laoreet nisl pulvinar. Etiam et ultrices erat. Fusce sit amet porttitor ex, sit amet tincidunt erat. Donec tincidunt purus eros, id porta purus tempor sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ultrices urna eget semper vestibulum. Mauris eu enim sed urna scelerisque porta accumsan at nibh. Sed consequat eros vitae mi volutpat venenatis. Sed et facilisis neque. Sed interdum mi vitae ligula interdum consectetur. Nunc libero sem, molestie non porttitor in, pulvinar ac risus. Quisque posuere vel neque eu laoreet. Nulla pretium ornare vehicula. Ut ornare justo eu blandit hendrerit.
Pellentesque at consectetur turpis, eget fringilla massa. Aliquam et leo in sapien efficitur lacinia nec et quam. Fusce ut varius sem, nec mollis neque. Duis id ante eu augue porttitor porta et nec tellus. Aliquam laoreet ullamcorper faucibus. Donec ac libero arcu. Aenean posuere eget sem in congue. Interdum et malesuada fames ac ante ipsum primis in faucibus. Proin tincidunt hendrerit scelerisque. Nunc aliquam lorem eget scelerisque mollis. Phasellus justo nisl, aliquet in ante id, aliquet suscipit diam. Nulla facilisi.
Curabitur ornare gravida urna. Nunc nisi tortor, molestie et ultricies vitae, condimentum a tellus. Curabitur feugiat gravida tristique. Nullam sodales elementum urna sit amet bibendum. Ut auctor tincidunt sem, sit amet aliquet justo. Maecenas vel libero sit amet odio egestas consequat. Sed id erat eget ipsum finibus molestie eget nec lacus. Praesent ut erat elementum, efficitur sapien a, tempor orci. Ut lacinia varius lorem vitae ullamcorper.
Mauris fringilla massa et pretium ultricies. Cras imperdiet, augue vitae mollis convallis, sapien elit condimentum lorem, eu egestas erat tellus sit amet lacus. Etiam sed mollis ipsum, ut hendrerit lacus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam ac blandit magna. Cras mi eros, fermentum a aliquam id, pulvinar ac risus. Quisque non efficitur lectus, eu consequat velit.
Pellentesque convallis vitae augue et dictum. Duis lectus enim, laoreet eu sollicitudin in, iaculis vitae ante. Donec a mollis enim. Sed a dolor nec neque iaculis molestie ac sit amet lectus. Mauris convallis condimentum magna. Fusce tempus faucibus ultricies. Duis dui tellus, tempor sit amet bibendum eget, facilisis ut orci. Vestibulum porttitor, diam ac fringilla vehicula, purus massa feugiat mi, vel fringilla neque ante a dui. Phasellus vel elit mi. In massa turpis, tristique vel dui sit amet, posuere aliquam risus. Integer sit amet orci sed lectus dignissim euismod. Nullam malesuada neque ut felis consequat aliquam. Duis lacinia mauris sit amet diam scelerisque fringilla. Morbi eu placerat lacus.
Donec in nisl justo. Curabitur vitae lectus a est pulvinar sollicitudin. Aenean risus lectus, malesuada sit amet mattis sit amet, vehicula ut nisl. Vestibulum non posuere nibh, id fringilla metus. Aenean at odio id erat posuere molestie. Etiam at eleifend lacus, in euismod orci. Morbi condimentum sem felis, vitae vulputate elit tincidunt vel. Aenean condimentum lorem eu mauris ullamcorper, cursus efficitur sapien malesuada. Nulla in varius sapien.
Etiam ac placerat ex. Etiam a efficitur mauris. Sed sit amet urna nunc. Quisque dapibus vehicula felis, eget hendrerit urna pretium non. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Quisque iaculis mauris velit, sit amet feugiat nisl tempor et. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam varius leo quis elit fringilla, non tincidunt magna molestie. Vivamus mauris lorem, mattis ac lorem ut, ultricies mattis ante. Quisque dapibus justo metus, non lobortis lectus porta ut. Praesent enim metus, finibus ut venenatis quis, eleifend a tortor.'''

pattern='finibus ut venenatis quis, eleifend a tortor'


solver = BoyerMooreSolution()
result = solver.strStr(text,pattern)
print(result)

print(ViolateSolution().strStr(text,pattern))

r'''
babbbbbabb
bbab
'''