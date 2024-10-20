# Turbo Tactical
This challenge is a simple FizzBuzz test to a remote server.

## Description
Players must send a modified FizzBuzz list to a remote server.

| Field | Value |
| ----- | ------ |
| Points | 50 |
| Created by | syyntax |
| Dependency | N/A |
| Attempts | 100 |

## Challenge
> The team at Turbo Tactical wants to try to infiltrate you into DEADFACE as a programmer. Thing is, DEADFACE is picky about who they bring in, so Turbo Tactical wants to make sure you're the real deal when it comes to programming.
>
> To prove yourself, write a program that will enumerate a list of numbers 1-500. For each number divisible by 3, replace it with TURBO. For each number divisible by 7, replace it with TACTICAL. For numbers divisible by both 3 AND 7, replace it with TURBOTACTICAL.  Feed this data into the server listed below and the flag will be revealed.
>
> <ip/hostname> 33000

> Submit the flag as `flag{flag_text}`

## Solution
This is a simple FizzBuzz test, except modified slightly using multiples of 3 and 7 instead of 3 and 5.

## Flag

flag{c0d3_wh1z_f1zzbuzz}
