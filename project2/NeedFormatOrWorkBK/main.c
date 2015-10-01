#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <openssl/evp.h>

int checkHash(unsigned char *hash){
    int i = 0;
    while (i<11){
        if (hash[i]=='\''){
            i++;
            if (hash[i]=='|'){
                i++;
                if (hash[i]=='|'){
                    i++;
                    if (hash[i]=='\''){
                        i++;
                        if (isdigit(hash[i])){
                            return 0;
                        }
                    }
                }
            }
            else if(hash[i]=='o'){
                i++;
                if (hash[i]=='r'){
                    i++;
                    if (hash[i]=='\''){
                        i++;
                        if (isdigit(hash[i])){
                            return 0;
                        }
                    }
                }
            }
        }
        else{
            i++;
        }
    }
    return 1;
}


int main()
{
    int input_length = 10;
    char inputString[input_length];
    static char possibleChar[] = "abcdefghijklmnopqrstuvwxyz0123456789";
    int randSelect = 0;

    srand(time(NULL)*32 + 2508957);


    EVP_MD_CTX mdctx;
    const EVP_MD *md;
    unsigned char outputHash[EVP_MAX_MD_SIZE];
    int output_length, i;

    OpenSSL_add_all_digests();
    md = EVP_get_digestbyname("MD5");

    if (!md){
        printf("not able to get MD5");
    }



    while (1){
        for (i=0; i<input_length; i++){
            randSelect = rand()%((int)(sizeof(possibleChar))-1);
            inputString[i] = possibleChar[randSelect];
        }

        EVP_MD_CTX_init(&mdctx);
        EVP_DigestInit_ex(&mdctx, inputString, strlen(inputString));
        EVP_DigestFinal_ex(&mdctx, outputHash, &output_length);
        EVP_MD_CTX_cleanup(&mdctx);

        printf("Digest is: ");
        for (i = 0; i< output_length; i++) printf("%02x", outputHash[i]);
        printf("\n");
        printf("Input was: ");
        for (i = 0; i <input_length; i++) printf("%c",inputString[i]);

        if(checkHash(outputHash) == 0){
            break;
        }
    }


    return 0;
}
