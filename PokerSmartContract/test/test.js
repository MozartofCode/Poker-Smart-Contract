// Import artifacts of the contracts
const Poker = artifacts.require('Poker');
const PlayLib = artifacts.require('PlayLib');
const CardLib = artifacts.require('CardLib');

contract('Poker', ([deployer, player1, player2]) => {

    let pokerInstance;
    let playLibInstance;
    let cardLibInstance;

    before(async () => {
        // Deploy CardLib and get its instance
        cardLibInstance = await CardLib.new({ from: deployer });

        // Link CardLib library to PlayLib
        await PlayLib.link('CardLib', cardLibInstance.address);
        // Deploy PlayLib and get its instance
        playLibInstance = await PlayLib.new({ from: deployer });

        // Link both CardLib and PlayLib to Poker
        await Poker.link('CardLib', cardLibInstance.address);
        await Poker.link('PlayLib', playLibInstance.address);

        // Deploy Poker and get its instance
        pokerInstance = await Poker.new(1000, 1000, { from: deployer });
    });

    describe('Poker Contract', () => {

        it('should correctly initialize players and deck', async () => {
            // Check initial balances of players
            const player1Balance = await pokerInstance.getPlayer1Balance();
            const player2Balance = await pokerInstance.getPlayer2Balance();
            assert.equal(player1Balance, 100, 'Player 1 balance is incorrect');
            assert.equal(player2Balance, 100, 'Player 2 balance is incorrect');

            // Check initial current bets of players
            const player1Bet = await pokerInstance.getPlayer1CurrentBet();
            const player2Bet = await pokerInstance.getPlayer2CurrentBet();
            assert.equal(player1Bet, 0, 'Player 1 current bet is incorrect');
            assert.equal(player2Bet, 0, 'Player 2 current bet is incorrect');

            // Check initial hands of players
            const player1Hand = await pokerInstance.getPlayer1Hand();
            const player2Hand = await pokerInstance.getPlayer2Hand();
            assert.equal(player1Hand[0].rank, '', 'Player 1 hand is incorrect');
            assert.equal(player1Hand[1].rank, '', 'Player 1 hand is incorrect');
            assert.equal(player2Hand[0].rank, '', 'Player 2 hand is incorrect');
            assert.equal(player2Hand[1].rank, '', 'Player 2 hand is incorrect');

            // Check initial table cards
            const table = pokerInstance.table;
            assert.equal(table.length, 5, 'Table cards length is incorrect');
            for (let i = 0; i < table.length; i++) {
                assert.equal(table[i].rank, '', `Table card ${i} rank is incorrect`);
            }
        });

        it('should correctly set and get player balances', async () => {
            await pokerInstance.setPlayer1Balance(1500);
            await pokerInstance.setPlayer2Balance(500);

            const player1Balance = await pokerInstance.getPlayer1Balance();
            const player2Balance = await pokerInstance.getPlayer2Balance();
            assert.equal(player1Balance, 1500, 'Player 1 balance is incorrect after setting');
            assert.equal(player2Balance, 500, 'Player 2 balance is incorrect after setting');
        });

        it('should correctly set and get player current bets', async () => {
            await pokerInstance.setPlayer1CurrentBet(100);
            await pokerInstance.setPlayer2CurrentBet(50);

            const player1Bet = await pokerInstance.getPlayer1CurrentBet();
            const player2Bet = await pokerInstance.getPlayer2CurrentBet();
            assert.equal(player1Bet, 100, 'Player 1 current bet is incorrect after setting');
            assert.equal(player2Bet, 50, 'Player 2 current bet is incorrect after setting');
        });

        it('should correctly set and get player hands', async () => {
            const player1Hand = [
                { rank: 'Ace', suit: 'Spades' },
                { rank: 'King', suit: 'Hearts' }
            ];
            const player2Hand = [
                { rank: 'Queen', suit: 'Diamonds' },
                { rank: 'Jack', suit: 'Clubs' }
            ];

            await pokerInstance.setPlayer1Hand(player1Hand);
            await pokerInstance.setPlayer2Hand(player2Hand);

            const retrievedPlayer1Hand = await pokerInstance.getPlayer1Hand();
            const retrievedPlayer2Hand = await pokerInstance.getPlayer2Hand();
            assert.equal(retrievedPlayer1Hand[0].rank, player1Hand[0].rank, 'Player 1 hand is incorrect after setting');
            assert.equal(retrievedPlayer1Hand[1].rank, player1Hand[1].rank, 'Player 1 hand is incorrect after setting');
            assert.equal(retrievedPlayer2Hand[0].rank, player2Hand[0].rank, 'Player 2 hand is incorrect after setting');
            assert.equal(retrievedPlayer2Hand[1].rank, player2Hand[1].rank, 'Player 2 hand is incorrect after setting');
        });

        // Add more tests as needed for other functions

    });

});
