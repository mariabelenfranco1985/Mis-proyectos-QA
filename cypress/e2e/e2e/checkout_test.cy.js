describe('Prueba de Checkout - SauceDemo', () => {
  it('Debería completar el proceso de compra correctamente', () => {

    // 1️⃣ Visitar la página de inicio
    cy.visit('https://www.saucedemo.com/')

    // 2️⃣ Iniciar sesión con credenciales válidas
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()

    // 3️⃣ Verificar que el login fue exitoso
    cy.url().should('include', '/inventory.html')

    // 4️⃣ Agregar un producto al carrito
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    // 5️⃣ Ir al carrito
    cy.get('.shopping_cart_link').click()

    // 6️⃣ Verificar que el producto está en el carrito
    cy.get('.inventory_item_name').should('contain', 'Sauce Labs Backpack')

    // 7️⃣ Hacer clic en el botón "Checkout"
    cy.get('[data-test="checkout"]').click()

    // 8️⃣ Verificar que estamos en la página del formulario del comprador
    cy.url().should('include', '/checkout-step-one.html')

    // 9️⃣ Completar los datos del comprador
    cy.get('[data-test="firstName"]').type('Maria')
    cy.get('[data-test="lastName"]').type('Franco')
    cy.get('[data-test="postalCode"]').type('1648')

    // 🔟 Continuar al resumen
    cy.get('[data-test="continue"]').click()

    // 11️⃣ Verificar que el producto aparece en el resumen
    cy.get('.inventory_item_name').should('contain', 'Sauce Labs Backpack')

    // 12️⃣ Finalizar compra
    cy.get('[data-test="finish"]').click()

    // 13️⃣ Verificar mensaje de confirmación
    cy.get('.complete-header').should('contain', 'Thank you for your order!')

  })
})
