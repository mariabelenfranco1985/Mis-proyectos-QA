describe('Prueba de agregar producto al carrito - SauceDemo', () => {

  it('Debería iniciar sesión y agregar un producto al carrito correctamente', () => {
    // 1️⃣ Ingresar al sitio
    cy.visit('https://www.saucedemo.com/')

    // 2️⃣ Iniciar sesión
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()

    // 3️⃣ Verificar login exitoso
    cy.url().should('include', '/inventory.html')
    cy.get('.title').should('contain', 'Products')

    // 4️⃣ Agregar el primer producto al carrito
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    // 5️⃣ Verificar que el ícono del carrito muestre 1 producto
    cy.get('.shopping_cart_badge').should('contain', '1')
  })

})

