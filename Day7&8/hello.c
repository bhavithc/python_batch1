


int add(int* a, int* b)
{
    return *a + *b; 
}


int main()
{

    int (*fptr)(int*, int*) = add;

    int a = 10;
    int b = 20;
    int c =  fpt(&a, &b);

}