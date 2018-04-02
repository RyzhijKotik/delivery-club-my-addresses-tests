email = "testuserdelivery@mail.ru"
password = "P@ssw0rd"
incorrect_addresses_list = ['С', 'Се', "λύφ", "'", "<script>alert('1')</script>", "javascript:alert('1')",
                        "`~!@#№%;^^&*()_-+=?/", '1234567890', '',
                        ''.join([""+str(ch) for ch in range(1, 100)])]
correct_addresses_list = ['заг']
housenumber_list = ['9']
unknown_addr_list = ["unknown"]