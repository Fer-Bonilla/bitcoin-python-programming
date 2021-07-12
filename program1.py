# This program uses bitcoinutils library to implement a program that get utx transactions 
# anb lock the bitcoin associated to them for a time defined by a blocks length.  
#
#

from bitcoinutils.setup import setup
from bitcoinutils.transactions import Transaction, TxInput, TxOutput, Sequence
from bitcoinutils.keys import P2pkhAddress, P2shAddress, PrivateKey
from bitcoinutils.script import Script
from bitcoinutils.constants import TYPE_RELATIVE_TIMELOCK
import click

def main():

    """ Implement your own agent to play knight's Isolation
    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.
    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.
    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    
    # Setup the bitcoin test network
    setup('testnet')

    # set the block time lock
    lock_length = 5    

    def validate_txinput_list(ctx, param, value):
        if value < 1:
            raise click.BadParameter("Should be correct utx transaction code or utx list.")
        return value

    def validate_lock_length(ctx, param, value):
        if value < 1 or value > 1000:
            raise click.BadParameter("Lock time parameter should be a number in the range 1, 1000.")
        return value
            
    @click.command()
    @click.option('--tx', default=1, callback=validate_txinput_list, help='List of Utx transactions to lock.')
    @click.option('--lt', default=1, help='Lock time parameter defined as the blocks lenght.')

    @click.argument('lines', default=-1, type=int)
    

    @click.version_option()
    def cli(count, foo, url):
        """Validation.
        This example validates parameters in different ways.  It does it
        through callbacks, through a custom type as well as by validating
        manually in the function.
        """
        if foo is not None and foo != "wat":
            raise click.BadParameter(
                'If a value is provided it needs to be the value "wat".',
                param_hint=["--foo"],
            )
        click.echo(f"count: {count}")
        click.echo(f"foo: {foo}")
        click.echo(f"url: {url!r}")    
    
    
    # @click.command()
    # @click.option(
    #     "--count", default=2, callback=validate_count, help="A positive even number."
    # )
    # @click.option("--foo", help="A mysterious parameter.")
    # @click.option("--url", help="A URL", type=URL())    


    # def hello(count, name):
    #     """Simple program that greets NAME for a total of COUNT times."""
    #     for x in range(count):
    #         click.echo(f"Hello {name}!")    
    
    
    # Get all the transacciones passed in the comandline
    #TxInput_list = sys.argv[1:]
    

    
    #for txInput in TxInput_list:
    
    # the UTXO of the P2SH-P2WPKH that we are trying to spend
    inp = TxInput('0061f744b654abfef7072e1e94de3b6c9e48100747b198e8aae9fb745555dcdc', 0)    
    
    
    #
    # This script creates a P2SH address containing a CHECKSEQUENCEVERIFY plus
    # a P2PKH locking funds with a key as well as for 20 blocks
    #
    
    #
    seq = Sequence(TYPE_RELATIVE_TIMELOCK, lock_length)

    # secret key corresponding to the pubkey needed for the P2SH (P2PKH) transaction
    p2pkh_sk = PrivateKey('cUcVVUeYgqciEXX9VMo7JPX9YYg5Btq7Jf4ojcZxQdR4R3nsXyRw')

    # get the address (from the public key)
    p2pkh_addr = p2pkh_sk.get_public_key().get_address()

    # create the redeem script
    redeem_script = Script([seq.for_script(), 'OP_CHECKSEQUENCEVERIFY', 'OP_DROP', 'OP_DUP', 'OP_HASH160', p2pkh_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG'])

    # create a P2SH address from a redeem script
    addr = P2shAddress.from_script(redeem_script)
    print(addr.to_string())

if __name__ == "__main__":
    main()