from pathlib import Path
import csv
house = Path.home()
file_path = house/"project_group"/"summary_report.txt"
file_path.touch()
print(file_path)
print(file_path.exists())
import api, cash_on_hand, overheads, profit_loss
def main():
  forex= api.api_function()
  overheads.Overheads_function(forex)
  cash_on_hand.coh_function(forex)
  profit_loss.profit_loss_function(forex)
  
main()
