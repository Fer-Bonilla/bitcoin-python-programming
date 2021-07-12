import click
from bitcoinutils.setup import setup
from bitcoinutils.transactions import Transaction, TxInput, TxOutput, Sequence
from bitcoinutils.keys import P2pkhAddress, P2shAddress, PrivateKey
from bitcoinutils.script import Script
from bitcoinutils.constants import TYPE_RELATIVE_TIMELOCK

# @click.group()
# def cli():
#   pass

# @click.group()
# def messages():
#   pass

#messages.add_command(generic)
#messages.add_command(welcome)


# Setup the bitcoin test network
setup('testnet')


def validate_txinput_list(ctx, param, value):
    click.echo(value)
    for val in value:
        if len(val) != 5:
            raise click.BadParameter("Should be correct utx transaction code or utx list.")
    return value

# def validate_lock_length(ctx, param, value):
#     if value < 1 or value > 1000:
#         raise click.BadParameter("Lock time parameter should be a number in the range 1, 1000.")
#     return value


#     @click.command()
#     @click.option('--tx', default=1, callback=validate_txinput_list help='List of Utx transactions to lock.')
#     @click.option('--lt', default=1, help='Lock time parameter defined as the blocks lenght.')



@click.command(name='tx')
#@click.argument('transactions', required=True, type=str)
@click.option('--tx', required=True, type=(str), callback=validate_txinput_list, help='List of Utx transactions to lock.')

#, cls=PythonLiteralOption, default=[])

#@click.option('--tx', default=False, required=True, type=str, help='List of Utx transactions to lock.')

#@click.command()
#@click.option('--data', required=True, type=(str, int))
def output(tx):
    click.echo([utx for utx in tx])



#def output(transactions, tx):
#    click.echo(transactions)

if __name__ == '__main__':
    output()
    #messages()