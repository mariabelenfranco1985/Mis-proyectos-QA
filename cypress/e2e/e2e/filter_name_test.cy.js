describe('Prueba de filtro por nombre de producto (A-Z y Z-A)', () => {
  
  beforeEach(() => {
    cy.visit('https://www.saucedemo.com/')
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()
    cy.url().should('include', '/inventory.html')
  })

  it('Verifica que el filtro A-Z ordena correctamente los productos', () => {
    cy.get('.product_sort_container').select('Name (A to Z)')
    cy.get('.inventory_item_name').then(($items) => {
      const nombres = [...$items].map(el => el.innerText)
      const nombresOrdenados = [...nombres].sort()
      expect(nombres).to.deep.equal(nombresOrdenados)
    })
  })

  it('Verifica que el filtro Z-A ordena correctamente los productos', () => {
    cy.get('.product_sort_container').select('Name (Z to A)')
    cy.get('.inventory_item_name').then(($items) => {
      const nombres = [...$items].map(el => el.innerText)
      const nombresOrdenados = [...nombres].sort().reverse()
      expect(nombres).to.deep.equal(nombresOrdenados)
    })
  })

})

