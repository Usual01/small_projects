#include <stdio.h>

int main()
{
    int number;
    int guess;

    number = 5;
    int i;

    for(i = 0; i < 3; i++)
    {
        printf("Guessed number %d ", i);
        scanf("%d", &guess);

        if(guess == number)
        {
            printf("you won");
            break;
        }
        
    }
    
    if(guess != number)
            printf("not correct");
        return 0;
    }
