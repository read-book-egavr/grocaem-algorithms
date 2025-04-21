class BinarySearch():

  def search_iterative(self, list, item):
    # low and high keep track of which part of the list you'll search in.
    # больше и меньше следите за тем, в какой части списка вы будите совершать поиск.
    low = 0                 # низкий
    high = len(list) - 1    # высокий
    # В этих переменных храним границы той части списка, в которой выполняется поиск.

    # While you haven't narrowed it down to one element ...
    # Пока мы не сузим границы до низа, до одного элемента
    while low <= high:
      # ... check the middle element
      # проверяем средний элемент
      mid = (low + high) // 2 # если значение нечетно, то Python автоматически 
      # округляет значение mid (середина) в меньшую сторону
      guess = list[mid]
      # Found the item.
      if guess == item: # тут мы смотрим предполагаемое значение равно или нет загаданному
        return mid      # если да, то возвращаем его индекс
      # The guess was too high.
      # Догадка была слишком большой
      if guess > item: # Если предполагаемое число слишком велико, то обновляется переменная high
        high = mid - 1
      # The guess was too low.
      # Догадка была слишком маленькой      
      else:
        low = mid + 1 # Если предполагаемое число слишком мало, то переменная low обновляется соответственно.

    # Item doesn't exist
    # Значение не существует вернем None
    return None

  def search_recursive(self, list, low, high, item):
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
        guess = list[mid]
  
        # If element is present at the middle itself 
        if guess == item:
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif guess > item: 
            return self.search_recursive(list, low, mid - 1, item) 
  
        # Else the element can only be present in right subarray 
        else: 
            return self.search_recursive(list, mid + 1, high, item) 
  
    else: 
        # Element is not present in the array 
        return None

if __name__ == "__main__":
  # We must initialize the class to use the methods of this class
  bs = BinarySearch()
  my_list = [1, 3, 5, 7, 9]
  
  print(bs.search_iterative(my_list, 3)) # => 1

  # 'None' means nil in Python. We use to indicate that the item wasn't found.
  print(bs.search_iterative(my_list, -1)) # => None