// Calculates the number of years it takes for a population to grow from a starting 
// size to a final size, based on a random population growth equation.

#include <stdio.h>
int main()
{
    int x;
    do
    {   
        printf("Enter starting population: ");
        scanf("%d", &x);
    }
    while (x < 9);
    
    int y;
    do
    {
        printf("Enter final population: ");
        scanf("%d", &y);
    }
    while (y < x);
    
    int a = 0;
    while (x < y)
    {
        x = x + (x / 4) - (x / 6);
        a++;
    }
    
    printf("It will take %i years to reach final population.", a);
}
