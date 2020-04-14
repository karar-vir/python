//WAP to find the largest between two or three numbers

class largestCheck
{
	public static void main(String..args)
	{
		int a=10,b=30,c=34;

		if (a>b)
		{
			if (a>c)
			{
				System.out.println("a is greater : ",a);
			}
			else
			{
				System.out.println("c is greater : ",c);
			}
		}
		else if (b>c)
		{
			System.out.println("b is greater : ",b);
		}
		else
		{
			System.out.println("c is greater : ",c);
		}
	}
}