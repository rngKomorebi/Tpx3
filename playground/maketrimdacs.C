void maketrimdacs()
{

//#col  row trim mask tp_ena
unsigned int trim[256][256], mask[256][256];


unsigned int row,col, _trim, _mask,_tp_ena;
unsigned int colmin=120; //80
unsigned int colmax=180; //190
unsigned int rowmin=140; //123
unsigned int rowmax=180; //233

TCanvas *c1=new TCanvas("c1","c1",1280,800);
c1->Divide(2,2);
TH2I *DACs=new TH2I("TRIMDACS","TRIMDACS",256,0,256,256,0,256);
TH2I *mask_before=new TH2I("MB","Mask bits before",256,0,256,256,0,256);
TH2I *mask_after=new TH2I("MA","Mask bits after",256,0,256,256,0,256);



FILE *in = fopen( "W0020_J07_trimdacs_template.txt" , "r");
 while (fscanf(in, "    %d %d %d %d %d #\n",&col, &row, &_trim, &_mask, &_tp_ena )!=EOF)
{
trim[col][row]=_trim;
mask[col][row]=_mask;




if( ((col<colmin)||(col>colmax))||((row<rowmin)||(row>rowmax))  ) mask[col][row]=1;


printf(" %d  %d  %d %d 0\n",col, row,_trim, mask[col][row]);


}

for(int col=0;col<256;col++)
for(int row=0;row<256;row++)
{
DACs->SetBinContent(col+1,row+1,trim[col][row]);
mask_after->SetBinContent(col+1,row+1,mask[col][row]);


}


c1->cd(1);
DACs->Draw("COLZ");

c1->cd(2);
mask_before->Draw("COLZ");

c1->cd(3);
mask_after->Draw("COLZ");



}


