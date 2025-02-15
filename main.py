from src.dtw_lab.lab1 import read_csv_from_google_drive, visualize_data, calculate_statistic



if __name__=='__main__':
    df = read_csv_from_google_drive('1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo')
    visualize_data(df)

    print(f'The mean value for the charge left percentage is {calculate_statistic('mean',df['Charge_Left_Percentage'])}')

from src . dtw_lab . lab1 import r e a d _ c s v _ f r o m _ g o o g l e _ d r i v e ,
visualize_data , calculate_statistic , cle an _d ata
if __name__ == ' __main__ ':
df = r e a d _ c s v _ f r o m _ g o o g l e _ d r i v e ('1
e K i A Z K b W T n r c G s 3 b q d h I N o 1 E 4 r B B p g l o')
df = cl ea n_ dat a ( df )
v i s u a l i z e _ d a t a ( df )
print ( f' The mean value for the charge left p er ce nta ge is
{ c a l c u l a t e _ s t a t i s t i c (' mean '
, df [' C h a r g e _ L e f t _ P e r c e n t a g e' ]) }
')