# my Partition Table plan *for my devices*


## Primary Partitions
```
123456789112345678921234567
BBbb # 12345 12345678901 ~~
0001 1 LiveO             5G
0010 2 VTESP VenToyEFISP 0i
0011 3 EFISP EFI.Sys.Ptn  B
0100 4 WinOS Windows C:\ 1
0101 5 WinRP WinRecovery 0G
0110 6 WinSP Win-EFI.S.P 0i
0111 7 MSwRP MS-Reserved  B
1000 8 Linux LinuxRoot /  L
1001 9 LBuVM Lnx:BakVMem  L
101x x LinEx /mnt/LinEx/ 2L
```
> L: Partition size of Linux

```
11xx
```

## Storage Partitions
```
123456789112345678921234567
### 123456 123456789112 ~~~

```
