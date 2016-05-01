#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
int n,a[100005];
int get(int left,int right)
{
    int minn=1e9+3;
    //得到当前子数组中最小值
    for(int i=left;i<=right;i++)
    {
        minn=min(minn,a[i]);
    }
    int ans=minn;
    int ii=0;
    for(int i=left;i<=right;i++)
    {
        if(a[i]==minn)
            continue;
        //a[i]不等于最小值时候
        ii=i+1;
        //下三行：计算子数组right
        while(ii<=right&&a[ii]!=minn)
            ++ii;
        ii--;
        //改变数组，统统减去最小值
        for(int j=i;j<=ii;j++)
            a[j]-=minn;
        ans+=get(i,ii);
        //调整left
        i=ii;
    }
    //竖着横着之间的最小值
    return min(right-left+1,ans);
}
int main()
{
    //freopen("in.txt", "r", stdin);
    while(~scanf("%d",&n))
    {
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        printf("%d\n",get(0,n-1));
    }
    return 0;
}
