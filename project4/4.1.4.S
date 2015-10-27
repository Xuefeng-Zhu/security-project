.global your_asm_fn
.section .data
coolfood: 
	.asciz "coolfood\0"
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp
push $0xc105ed
mov %esp, %eax
push $coolfood
push %eax
push $0xacce55ed
call practice
mov %ebp, %esp
pop %ebp


leave
ret
