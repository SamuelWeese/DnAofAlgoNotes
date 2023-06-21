long long recusiveCalc(int x, int p)
{
    long long answer = 1;

    // Odd Case
    if (p%2 == 1)
    {
        
    }

    return recusiveCalc(x, p);
}

long long loopCalc(int x, int p)
{
    long long answer = x;
    // loop size will always be p-1
    for (int i = 1; i < p; i++)
    {
        answer *= x;
    }
    return answer;
}



long long binaryCalc(int x, int p)
{
    long long answer;
}
