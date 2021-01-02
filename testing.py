import timeit
import example_cy

cy = timeit.timeit('example_cy.test(500)', setup="import example_cy", number=5000)
py = timeit.timeit('example_py.test(500)', setup="import example_py", number=5000)

print(py, cy)
print(f"Cython is {py/cy} faster than Python")
