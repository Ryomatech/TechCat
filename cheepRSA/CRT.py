from math import gcd
import random

prime_list = [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
str_list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','?',',','.',',',':']


def lcm(p,q):
    return (p*q) // gcd(p,q)

def generate_keys(p,q):
    N=p*q
    L=lcm(p-1,q-1)
    for i in range(2,L):
        if gcd(i,L) == 1:
            E = i
            break
    
    for i in range(2,L):
        if (E*i) % L == 1:
            D = i
            break
    return (E,N) , (D,N)

def encrypt(plain_text,public_key):
    E,N = public_key
    plain_integers = [str_list.index(char) for char in plain_text]
    encrypted_integers = [pow(i, E, N) for i in plain_integers]
    fill_encrypted_integers = [str(i).zfill(6) for i in encrypted_integers]
    return fill_encrypted_integers

def create_crypt_sentence(text):
    public_key, private_key = generate_keys(create_pair()[0],create_pair()[1])
    fill_encrypted_integers = encrypt(text,public_key)
    D,N=private_key
    D,N = str(D).zfill(6),str(N).zfill(6)
    num = random.randint(0, min(len(fill_encrypted_integers),9))
    fill_encrypted_integers.insert(num,D)
    fill_encrypted_integers.insert(num,N)
    fill_encrypted_integers.insert(0,str(num))
    return ''.join(fill_encrypted_integers)


def create_pair():
    pair = random.sample(prime_list,2)
    if  pair[0]*pair[1]>=100000 and pair[0]*pair[1]<1000000:
        return pair
    else:
        return create_pair()


def decrypt(crypt_sentence):
    num = int(crypt_sentence[0])
    crypt_sentence = crypt_sentence[1:]
    split_crypt_sentence = [crypt_sentence[i:i+6] for i in range(0, len(crypt_sentence), 6)]
    N = split_crypt_sentence[num]
    split_crypt_sentence.pop(num)
    D = split_crypt_sentence[num]
    split_crypt_sentence.pop(num)
    D,N = int(D),int(N)
    encrypted_integers = [int(i) for i in split_crypt_sentence]
    decrypted_intergers = [pow(i, D, N) for i in encrypted_integers]
    decrypted_str = [str_list[i] for i in decrypted_intergers]
    decrypted_text = ''.join(decrypted_str)
    return decrypted_text


#print(create_crypt_sentence(text))
print(decrypt(str(input())))

