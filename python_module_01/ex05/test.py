# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/07 13:28:07 by lguisado          #+#    #+#              #
#    Updated: 2023/06/07 13:38:08 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from the_bank import Bank, Account

if __name__ == '__main__':
	print('--- 01.05.01 ---')
	bank = Bank()
	john = Account('John', zip='1234', brother='James', value=6460.0, ref='23432f32234f324g425542g', info=None,
				   other='This is ...', lol='hihi')
	bank.add(john)
	print(f' Is corrupted john? {john._is_corrupted()}')
	bank.fix_account('John')
	print(f' Fixed: Is corrupted john? {john._is_corrupted()}')
	print('--- 01.05.02 ---')
	john = Account('William John', zip='100-064', rother="heyhey", ref='58ba2b9954cd278eda8a84147ca73c87', info=None, other='This is the vice president of the corporation', lol = "lolilol")
	print(f' Is corrupted john? {john._is_corrupted()}')
	print('--- 01.05.04 ---')
	bank = Bank()
	bank.add(Account('Jane', zip='911-475', value=1000.0, ref='23432f32234f324f425542f'))
	john = Account('John', zip='911-475', value=1000.0, ref='23432f32234f324c425542b')
	bank.add(john)
	print(' testing a valid transfer')
	print(f'  John value={john.value}')
	print(f"  transfer worked? {bank.transfer('Jane', 'John', 500)}")
	print(f'  John value={john.value}')
	print('--- 01.05.05 ---')
	print(f" transfer worked? {bank.transfer('Jane', 'John', 1000)}")
	print(f' John value={john.value}')