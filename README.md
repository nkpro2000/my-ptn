# my Partition Table plan *for my devices*


## Primary Partitions
```
123456789112345678921234567
BBbb # 12345 12345678901 ~~
0001 1 LiveO             5G -> /ptn/v/main/ AND /ptn/1/
0010 2 VTESP VenToyEFISP 0i -> /ptn/v/esp/
0011 3 EFISP EFI.Sys.Ptn  B :: /boot/efi/ OR /efi/
0100 4 WinOS Windows C:\ 1  -> /ptn/w/main/
0101 5 WinRP WinRecovery 0G
0110 6 WinSP Win-EFI.S.P 0i -> /ptn/w/esp/
0111 7 MSwRP MS-Reserved  B
1000 8 Linux LinuxRoot /  L :: /
1001 9 LBuVM Lnx:BakVMem  L :: /ptn/l/bak/
101x x LinEx /mnt/LinEx/ 2L -> /mnt/LinEx/
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
