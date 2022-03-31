# Sugar tracker

This program allows you to track the price of 1 kg of sugar in Russia, based on [sbermegamarket.ru](https://sbermegamarket.ru/) data.

## Usage

Install the requirements and just run `sugar_tracker.py`. Add the `-j` or `--json` argument to get JSON output.

## Example

```
> python ./sugar_tracker.py   
Prices per 1 kg according to https://sbermegamarket.ru/catalog/sahar/ data:
mean: 102.64 ₽
min: 85.0 ₽ (Сахар песок белый Продимекс 1 кг)
max: 121.11 ₽ (Сахар Rioba свекловичный белый песок 900 г

> python ./sugar_tracker.py --json
{
  "mean_price": 102.64,
  "min_price": 85.0,
  "min_name": "Сахар песок белый Продимекс 1 кг",
  "max_price": 121.11,
  "max_name": "Сахар Rioba свекловичный белый песок 900 г",
  "source": "https://sbermegamarket.ru/catalog/sahar/"
}
```
