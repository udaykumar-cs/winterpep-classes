
# Immutable example
def change(x):
    x += 10   # changes local copy only

a = 5
change(a)
print(a)     # 5 → integer is immutable, original value unchanged

# Mutable example
def update(lst):
    lst.append(10)  # modifies the original list

nums = [1, 2, 3]
update(nums)
print(nums)       # [1, 2, 3, 10] → list is mutable, original list changed

