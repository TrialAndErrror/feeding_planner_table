import datetime

from rich.console import Console
from rich.table import Table


def main():
    total_volume = 300

    table = Table(title=f"Feeding Planner: {total_volume} mL")

    table.add_column("Rate", justify="right", style="grey53", no_wrap=True)

    for num in range(5):
        table.add_column(f"Start ({num + 1})", style="plum4")
        table.add_column(f"End ({num + 1})", justify="right", style="green4")

    hours_delay = 1

    delay = datetime.timedelta(hours=hours_delay)
    time_format = "%I:%M %p"

    base_rate = 45

    for num in range(10):
        rate = base_rate + (2 * num)
        total_time = datetime.timedelta(hours=(total_volume / rate))

        columns = [
            f"{rate}",
        ]
        for instance in range(5):
            extra_delay = datetime.timedelta(minutes=(15 * instance))
            start_time = datetime.datetime.now() + delay + extra_delay
            end_time = datetime.datetime.now() + delay + total_time + extra_delay

            columns.extend([
                f"{start_time.strftime(time_format)}",
                f"{end_time.strftime(time_format)}"])

        table.add_row(
            *columns
        )

    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()
