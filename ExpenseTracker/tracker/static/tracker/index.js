const balance = document.getElementById('balance');
const money_plus = document.getElementById('money-plus');
const money_minus = document.getElementById('money-minus');
const list = document.getElementById('list');
const form = document.getElementById('form');
const text = document.getElementById('text');
const amount = document.getElementById('amount');

var transactions = []

// Add transaction
const addTransaction = async (e) => {
  e.preventDefault();

  if (text.value.trim() === '' || amount.value.trim() === '') {
    alert('Please add a text and amount');
  } else {
    const transaction = {
      title: text.value,
      quantity: amount.value,
      add_money: "Income"
    };

    console.log(transaction)
    const res = await fetch(`api/expense-add/`, 
        { method:'POST', 
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(transaction),
    })

    transactions.push(transaction);
    addTransactionDOM(transaction);

    text.value = '';
    amount.value = '';
  }
}

// Add transactions to DOM list
function addTransactionDOM(transaction) {
  // Get sign
  const sign = transaction.add_money == 'Expense' ? '-' : '+';
  console.log(transaction.add_money, sign)

  const item = document.createElement('li');

  // Add class based on value
  item.classList.add(sign == '-' ? 'minus' : 'plus');

  item.innerHTML = 
  `${transaction.title} <span>${sign}${Math.abs(transaction.quantity)}</span> 
    <button class="delete-btn" onclick="removeTransaction(${transaction.id})">x</button>
  `;

  list.appendChild(item);
}

// Update the balance, income and expense
function updateValues() {
  const amounts = transactions.map(transaction => transaction.add_money == "Income" ? transaction.quantity : -transaction.quantity);
  const total = amounts.reduce((acc, item) => (acc += item), 0).toFixed(2);

  const income = amounts
    .filter(item => item > 0)
    .reduce((acc, item) => (acc += item), 0)
    .toFixed(2);

  const expense = (
    amounts.filter(item => item < 0).reduce((acc, item) => (acc += item), 0) * -1
    ).toFixed(2);

  balance.innerText = `$${total}`;
  money_plus.innerText = `$${income}`;
  money_minus.innerText = `$${expense}`;
}

// Remove transaction by ID
const removeTransaction = async (id) => {
    await fetch(`api/expense-delete/${id}`,
        {method:'DELETE',})

  transactions = transactions.filter(transaction => transaction.id !== id);
  init();
}

const getTransactions = async () => {
    const res = await fetch('api/expense-list')
    const data = await res.json()

    return data;
}

// Init app
async function init() {
  list.innerHTML = '';

  transactions = await getTransactions();

  transactions.forEach(addTransactionDOM);
  updateValues();
}

init();

form.addEventListener('submit', addTransaction);