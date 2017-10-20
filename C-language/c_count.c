#include<stdio.h>

int main()
{
    int spacenum = 0;
    int tabnum = 0;
    int enternum = 0;
    int wordnum = 0;
    int c = 0;

    c = getchar();
    while( c!= '0' ){
        if(' ' == c)
        {
            spacenum++;
        }
        else if('\t' == c)
        {
            tabnum++;
        }
        else if('\n' == c)
        {
            enternum++;
        }
        else if((c < 91 && c >64) || (c>96 && c<123))
        {
            wordnum++;
        }
        else
        {
            printf("unknow\n");
        }
        //putchar(c);
        c = getchar();
    }
    printf("space = %d\n",spacenum);
    printf("tab = %d\n",tabnum);
    printf("enter = %d\n",enternum);
    printf("word = %d\n",wordnum);
    return 0;
}
