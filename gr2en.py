#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# translate greek names to greeklish

import re
import sys
from codecs import open

def g2e(s):
    # Δίφθογγοι αυ, ευ, ηυ
    s = re.sub(u'([αεηΑΕΗ])[υύ](βγδζλμνραιυεοηωάίύέόήώϊϋΒΓΔΖΛΜΝΡΑΙΥΕΟΗΩΆΊΎΈΌΉΏΪΫ])', r'\1v\2', s)
    s = re.sub(u'([αεηΑΕΗ])[ΥΎ]([βγδζλμνραιυεοηωάίύέόήώϊϋΒΓΔΖΛΜΝΡΑΙΥΕΟΗΩΆΊΎΈΌΉΏΪΫ])', r'\1V\2', s)
    s = re.sub(u'([αεηΑΕΗ])[υύ]([θκξπστφχψΘΚΞΠΣΤΦΧΨ\b])', r'\1f\2', s)
    s = re.sub(u'([αεηΑΕΗ])[ΥΎ]([θκξπστφχψΘΚΞΠΣΤΦΧΨ\b])', r'\1F\2', s)

    s = re.sub(u'ο[υύ]', r'ou', s)
    s = re.sub(u'Ο[ΥΎ]', r'OU', s)
    s = re.sub(u'Ο[υύ]', r'Ou', s)

    s = re.sub(u'γγ', r'ng', s)
    s = re.sub(u'ΓΓ', r'NG', s)

    s = re.sub(u'γχ', r'nch', s)
    s = re.sub(u'ΓΧ', r'NCH', s)

    s = re.sub(u'γξ', r'nx', s)
    s = re.sub(u'ΓΞ', r'NX', s)

    s = re.sub(u'μπ', r'b', s)
    s = re.sub(u'ΜΠ', r'B', s)
    s = re.sub(u'Μπ', r'B', s)

    s = re.sub(u'θ', r'th', s)
    s = re.sub(u'Θ', r'TH', s)

    s = re.sub(u'χ', r'ch', s)
    s = re.sub(u'Χ', r'CH', s)

    s = re.sub(u'ψ', r'ps', s)
    s = re.sub(u'Ψ', r'PS', s)

    s = re.sub(u'α', r'a', s)
    s = re.sub(u'Α', r'A', s)
    s = re.sub(u'β', r'v', s)
    s = re.sub(u'Β', r'V', s)
    s = re.sub(u'γ', r'g', s)
    s = re.sub(u'Γ', r'G', s)
    s = re.sub(u'δ', r'd', s)
    s = re.sub(u'Δ', r'D', s)
    s = re.sub(u'ε', r'e', s)
    s = re.sub(u'Ε', r'E', s)
    s = re.sub(u'ζ', r'Z', s)
    s = re.sub(u'Ζ', r'Z', s)
    s = re.sub(u'η', r'i', s)
    s = re.sub(u'Η', r'I', s)
    s = re.sub(u'ι', r'i', s)
    s = re.sub(u'Ι', r'I', s)
    s = re.sub(u'κ', r'k', s)
    s = re.sub(u'Κ', r'K', s)
    s = re.sub(u'λ', r'l', s)
    s = re.sub(u'Λ', r'L', s)
    s = re.sub(u'μ', r'm', s)
    s = re.sub(u'Μ', r'M', s)
    s = re.sub(u'ν', r'n', s)
    s = re.sub(u'Ν', r'N', s)
    s = re.sub(u'ξ', r'X', s)
    s = re.sub(u'Ξ', r'X', s)
    s = re.sub(u'ο', r'o', s)
    s = re.sub(u'Ο', r'O', s)
    s = re.sub(u'π', r'p', s)
    s = re.sub(u'Π', r'P', s)
    s = re.sub(u'σ', r's', s)
    s = re.sub(u'ρ', r'r', s)
    s = re.sub(u'Ρ', r'R', s)
    s = re.sub(u'Σ', r'S', s)
    s = re.sub(u'τ', r't', s)
    s = re.sub(u'Τ', r'T', s)
    s = re.sub(u'υ', r'Y', s)
    s = re.sub(u'Υ', r'Y', s)
    s = re.sub(u'φ', r'f', s)
    s = re.sub(u'Φ', r'F', s)
    s = re.sub(u'ω', r'o', s)
    s = re.sub(u'Ω', r'O', s)
    s = re.sub(u'ά', r'a', s)
    s = re.sub(u'Ά', r'A', s)
    s = re.sub(u'ί', r'i', s)
    s = re.sub(u'Ί', r'I', s)
    s = re.sub(u'ύ', r'y', s)
    s = re.sub(u'Ύ', r'Y', s)
    s = re.sub(u'έ', r'e', s)
    s = re.sub(u'Έ', r'E', s)
    s = re.sub(u'ό', r'o', s)
    s = re.sub(u'Ό', r'o', s)
    s = re.sub(u'ή', r'i', s)
    s = re.sub(u'Ή', r'I', s)
    s = re.sub(u'ώ', r'o', s)
    s = re.sub(u'Ώ', r'O', s)
    s = re.sub(u'ϊ', r'i', s)
    s = re.sub(u'Ϊ', r'I', s)
    s = re.sub(u'ϋ', r'y', s)
    s = re.sub(u'Ϋ', r'Y', s)
    s = re.sub(u'ΐ', r'i', s)
    s = re.sub(u'ΰ', r'y', s)
    s = re.sub(u'ς', r's', s)
    
    return s
    

if __name__ == '__main__':

    for file in sys.argv[1:]:
        try:
            f = open(file, encoding='utf-8')
            for line in f:
                print g2e(line)
        finally:
            f.close()
